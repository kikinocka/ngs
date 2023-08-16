#!/usr/bin/env python3

#courtesy of github.com/morpholino

import sys,gzip

infile = sys.argv[1]

print("This script reformats interproscan gff3 files for ones suitable for Geneious import")
print("It also removes duplicate sequences (can be useful)")
print("usage: python interproscan-gff2geneious.py <path/to/file>\n--------------------------------------------------------------------------")

#########################
####       Fx        ####
#########################

def get_interpro_version(file):
	with open(file) as f:
		head = [next(f) for _ in range(5)]
	versline = [x for x in head if x.startswith("##interproscan-version")][0]
	version = versline.split()[-1]
	print(f"{version} InterProScan")
	return version


def read_panther_families(interproversion="5.57-90.0"):
	pantherversion = {"": "PANTHER17.0_HMM_classifications.gz",
					  "5.52-86.0": "PANTHER15.0_HMM_classifications.gz",
					  "5.57-90.0": "PANTHER15.0_HMM_classifications.gz",
					  "5.59-91.0": "PANTHER16.0_HMM_classifications.gz",
					  "5.61-93.0": "PANTHER17.0_HMM_classifications.gz",
					  }
	pantherfile = pantherversion[interproversion]
	with gzip.open(pantherfile, "rt") as f:
		panther_db = {x.split("\t")[0]: x.split("\t")[1] for x in f}
	return panther_db


def delbadchars(string):
	badchars = ("|+,:;()' ") #also []/@
	n = []
	for c in string:
		if c in badchars:
			c = "_"
		n.append(c)
	result = "".join(n)
	return result


def is_tool(name):
    """Check whether `name` is on PATH and marked as executable."""

    # from whichcraft import which
    from shutil import which

    return which(name) is not None


def parse_annotations(string):
	line = string.strip().split("\t")
	if line[2] == "polypeptide":
		writestring = ""
	elif line[1] in ["CDD", "Gene3D", "TIGRFAM", "PIRSF", "SFLD", "Coils", "ProDom", "SUPERFAMILY", "SMART"]:
		writestring = ""
	else:
		target, program, database, left, right, evalue, direction, frame, annot = line[0], "IPSparser", line[1], line[3], line[4], line[5], ".", line[7], line[8]
		if ";" in annot:
			annots = annot.split(";")
			newannots = []
			if "signature_desc" in annot:
				is_newname = True
			else:
				is_newname = False
			for a in annots:
				if a.startswith("date") or a.startswith("Target") or a.startswith("ID"):
					#these are added InterProScan information
					pass
				elif a.startswith("signature_desc"):
					#signature description gives a good name, put that in front
					a = a.replace("signature_desc", "Name")
					newannots = [a] + newannots
				elif a.startswith("Name"):
					#if there is a valid signature description
					if is_newname == True:
						#if there is a valid Pfam signature description, we derive a name from there
						#since we cannot have two names in one line, this is the Pfam id
						a = a.replace("Name", "Id")
						newannots += [a]
					#else if this is a panther family
					elif "PTHR" in a:
						#most likely this is a panther family
						#get name from panther_db based on panther code
						#then append Name and panther code if applicable
						a = a.replace("Name=", "")
						name = panther_db.get(a, a)
						if name != a:
							newannots += ["Name=" + name, "Id=" + a]
						else:
							newannots += ["Name=" + a]
					#whatever else, this is probably good as it is
					else:
						newannots += [a]
				else:
					newannots += [a]
			annot = ";".join(newannots)
		else:
			print("; not in annotation?")

		writestring = "\t".join([target, program, database, left, right, evalue, direction, frame, annot]) + "\n"
	return(writestring)


def parse_fasta(seqname, sequence):
	if seqname.startswith(">match"):
		writestring = ""
	else:
		writestring = "{}\n{}\n".format(seqname, "\n".join(sequence))
		
	return(writestring)


#########################
#### Read parameters ####
#########################

filelist = [infile]

print("IPSparser: Files to be analyzed: {}".format(", ".join(filelist)) )

interproversion = get_interpro_version(infile)

global panther_db
panther_db = read_panther_families(interproversion)
print(len(panther_db), "Panther items")

for file in filelist:
	print("IPSparser: Opening file {}".format(file))
	filename = file.split(".")[0]
	seqlist = set()
	with open(file) as f, open(filename + "_geneious.gff3", "w") as out:
		print("IPSparser: Parsing annotations...")
		annotation = True #we start in the annotation section
		firstseq = True
		for line in f:
			line = line.strip()
			#now to information parsing
			if line == "##FASTA":
				annotation = False

			if annotation == True:
				#each annotation is one-line
				if line.startswith("##"):
					writestring = line + "\n"
				else:
					writestring = parse_annotations(line)
				out.write("{}".format(writestring))
			elif line == "##FASTA":
				#entering sequence section, turn off annotation-like parsing
				print("IPSparser: Now for something completely different. Parsing sequences...")
				out.write("##FASTA\n")
			else:
				#in the sequence section, parse FASTA-like data
				if line.startswith(">"):
					if not firstseq:
						#sequence loading done, new sequence header found
						writestring = parse_fasta(seqname, sequence)
						if seqname not in seqlist:
							seqlist.add(seqname)
							out.write(writestring)
					sequence = []
					seqname = line
				else:
					sequence.append(line)
					firstseq = False #now we have at least one
		#make sure the last sequence is written
		if seqname not in seqlist:
			writestring = parse_fasta(seqname, sequence)
			out.write(writestring)

print("IPSparser: Finished.")		


