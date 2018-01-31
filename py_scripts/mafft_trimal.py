# Performs fasta header renaming, and calls mafft and trimal to align and trim datasets 
# automatically on all fasta files in the current folder
# Alternatively, set folder with -d

import os
import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser(description='How to use argparse')
parser.add_argument('-d', '--directory', help='Working directory', default='.')
args = parser.parse_args()
directory = args.directory

files = os.listdir('.')
files = [f for f in files if f.endswith(".fasta")]
#skip = ["unwanted_species"]
filecount = len(files)

fnames = set()
for f in files:
	leaves = []
	fname = f.split(".fasta")[0]
	fnames.add(fname)
	with open(fname + "-safe.fst", "w") as outsafefile, open(fname + "-trans.tsv", "w") as outtransfile:
		for sequence in SeqIO.parse(f, "fasta"):
			safeleaf = str(sequence.name).split("_")[0]
			leaves.append(safeleaf)
			if leaves.count(safeleaf) > 1:
				count = leaves.count(safeleaf)
				safeleaf = safeleaf + str(count)
			outsafefile.write(">{}\n{}\n".format(safeleaf, sequence.seq))
			outtransfile.write("{}\t{}\n".format(safeleaf, sequence.description))
	print("File {} processed".format(f))

print("Writing sequences done, now to alignment and trimming...")

zerosizefiles = []
for f in fnames:
	fname = f + "-safe.fst"
	if os.stat(fname).st_size > 0:
		os.system("mafft --maxiterate 1000 --localpair --thread 3 {0}-safe.fst > {0}.linsi".format(f))
		os.system("trimal -in {0}.linsi -out {0}.MaffTrimal.fst -fasta -automated1".format(f))
	else:
		zerosizefiles.append(fname)

for fname in zerosizefiles:
	if os.stat(fname).st_size > 0:
		os.system("mafft --maxiterate 1000 --localpair --thread 3 {0}-safe.fst > {0}.linsi".format(fname))
		os.system("trimal -in {0}.linsi -out {0}.MaffTrimal.fst -fasta -automated1".format(fname))
	else:
		print("Could not process {}. Zero bytes in file".format(fname))
