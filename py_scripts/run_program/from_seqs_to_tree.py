#!/usr/bin/env python3
import os
from Bio import SeqIO,AlignIO
import argparse
import re

parser = argparse.ArgumentParser(description='How to use argparse')
parser.add_argument('-i', '--infile', help='Fasta/Phylip set to be analyzed', default="batch")
parser.add_argument('-a', '--aligner', help='Aligner', default='run_pasta.py')
parser.add_argument('-t', '--treemaker', help='Program for tree inference', default='none')

args = parser.parse_args()

home = "/Volumes/zoliq data/OwnCloud/"
os.chdir(home + "genomes/euglena gracilis/trees")
for generation in range(1,15):
	if os.path.isdir("TREE" + str(generation)) == False:
		outdir = "TREE" + str(generation)
		break

allowed = ("fasta", "fas", "fst", "phy", "phylip")
if args.infile == "batch":
	infilelist = [x for x in os.listdir(".") if x.split(".")[-1] in allowed]
	infilelist = [x for x in infilelist if not x.startswith("safe")] #bc these have been created by a previous run
	infilelist = [x for x in infilelist if not x.startswith("trim")] #bc these have been created by a previous run
elif args.infile.split(".")[-1] in allowed:
	infilelist = [args.infile]
else:
	quit("file type not recognized - is it fasta/fas/fst or phy/phylip?")

print("Files to be analyzed: " + ", ".join(infilelist))
print("Data output to dir: " + outdir)

badchars = ("|@+,:;()'") #also []/
taxonpattern = r'\[(.+)\]'
for file in infilelist:
	print("Processing file: " + file)
	extension = file.split(".")[-1]
	filename = file.replace("." + extension, "")
	if extension in ("fasta", "fas", "fst"):
		indataset = SeqIO.parse(file, 'fasta')
	elif extension in ("phy", "phylip"):
		indataset = SeqIO.parse(file, 'phylip')
	else:
		continue
	#load fasta
	seq_d = {}
	seq_set = set()
	with open("error.log", "a") as error:
		errors = False
		for sequence in indataset:
			fullname = sequence.description
			newname = []
			for c in fullname:
				if c in badchars:
					c = "_"
				newname.append(c)
			shortname = ''.join(newname)
			taxonmatch = re.search(taxonpattern, shortname)#.group(1)
			if taxonmatch:
				taxon = taxonmatch.group(1)
				if sequence.name.startswith(taxon):
					shortname = shortname.replace("[{}]".format(taxon), "")
					fullname = fullname.replace("[{}]".format(taxon), "")
			safeseq = str(sequence.seq).replace("*","")
			if shortname not in seq_d:
				if safeseq not in seq_set:
					seq_d[shortname] = (fullname, safeseq)
				else:
					errors = True
					error.write("duplicate sequence, skipping:\n{}\n{}\n".format(shortname, safeseq))
			else:
				errors = True
				error.write("seq name not unique, skipping:\n{0}\n{1}\n{0}\n{2}\n".format(shortname, safeseq, seq_d[shortname][1]))
			#print(">" + shortname + "\n" + seq_d[shortname])
	if errors:
		print("Errors occurred during sequence read, please refer to error.log")

	print("done loading sequences, now to writing safe_file...")
	with open("rename-{}.txt".format(filename), "w") as renaming, open("safe-{}.fasta".format(filename), "w") as safefile:
		for key,value in seq_d.items():
			renaming.write("{}\t{}\n".format(key, value[0]))
			safefile.write(">{}\n{}\n".format(key, value[1]))

	command = "{0} -d protein -i safe-{1}.fasta -j {1} -o {2}".format(args.aligner, filename, outdir)
	print("issuing aligner\n" + command)
	os.system(command)

	#copy and rename PASTA alignment to current directory and issue trimal
	os.system("cp ./{1}/{0}.marker001.safe-{0}.aln ./safe-{0}.aln".format(filename, outdir))
	os.system("trimal -in ./safe-{0}.aln -out trim-{0}.aln -fasta -automated1".format(filename)) #-gappyout / -automated1 / -gt 0.3
	print("issuing: trimal -in ./safe-{0}.aln -out trim-{0}.aln -fasta -automated1".format(filename))

	#open trimal-trimmed alignment for dumping any gaps-only sequences
	trimalignmentfile = AlignIO.read("trim-{0}.aln".format(filename), "fasta")
	outfile1, outfile2 = "trimfilt-{0}.fasta".format(filename), "trimfilt-{0}.phy".format(filename)
	#filter out any sequences that are gaps-only after trimming
	filtalignmentfile = [record for record in trimalignmentfile if record.seq.count("-") != len(record.seq) and len(record.seq) != 0]
	with open(outfile1, "w") as result:
		for index, r in enumerate(filtalignmentfile):
			#get rid of the trailing newline character at the end of file:
			if index != len(filtalignmentfile) - 1:
				result.write(">{}\n{}\n".format(r.description, r.seq))
			else:
				result.write(">{}\n{}".format(r.id, r.seq))
		#count number of remaining sequences and their length
		count, length = len(filtalignmentfile), len(r.seq)

	#convert trimfile to phylip format (phylobayes)
	if os.stat(outfile1).st_size > 0: #check for file size
		ffile = AlignIO.read(outfile1, "fasta")
		AlignIO.write(ffile, outfile2, "phylip-relaxed")
	else:
		print("#####\nWARNING: File {} has zero size\n#####".format(outfile1))

	print("Automated trimming done. Hooray!\nTrimming produced a file with {} sequences of {} sites\n\n".format(count, length))

	if args.treemaker != "none":
		if args.treemaker == "iqtree-omp":
			treecommand = "-m TEST -mset LG -nt AUTO -s trimfilt-{}.fasta".format(filename)
		os.system("{} {}".format(args.treemaker, treecommand))
