#!/usr/bin/env python3

#courtesy of github.com/morpholino

import os, re, argparse
from Bio import SeqIO, AlignIO

def read_tag(nodename):
	partpattern = r'_([\.\d]+)%aligned'
	try:
		taghit = re.search(partpattern, nodename)
		tag = taghit.group()
		perc = float(taghit.group(1))
		#nodename = nodename.replace(tag, "")
	except:
		perc = 101
		tag = ""
		#print(f"No pattern in {nodename}")
	return perc


def coverage(infile):
	coverage_d = {}
	with open(infile, "rt") as f:
		for l in f:
			l = l.strip().split("\t")
			if len(l) == 3:
				coverage_d[l[1]] = read_tag(l[2])
	return coverage_d


def coverage_from_alignment(infile, fileformat):
	"""Trims an alignment Fasta, using a filter
	list to trash unwanted results. Also, sequences
	with high number of unknowns are removed.
	
	Args:
		infile:			Input fasta name
			
	Returns:
		coverage_d: 	Dictionary with alignment coverage
	
	"""

	coverage_d = {}
	alignment = AlignIO.read(infile, fileformat)
	length = alignment.get_alignment_length()
	badchars = ("-", "X")
	for s in alignment:
		seq = "".join([x for x in s.seq if x not in badchars])
		coverage_d[s.name] = 100*(len(seq)/length)
	return coverage_d


def filter_alignment(infile, threshold, coverage_d):
	outfile = infile.split(".aln")[0] + ".filtered-{}.aln".format(int(threshold))
	with open(outfile, "wt") as result:
		for seq in SeqIO.parse(infile, "fasta"):
			if "%aligned" in seq.name:
				aligned = read_tag(seq.name)
				if aligned < threshold:
					continue
				result.write(">{}\n{}\n".format(seq.name, seq.seq))
			elif seq.name in coverage_d:
				aligned = coverage_d.get(seq.name, 101)
				if aligned < threshold:
					continue
				result.write(">{}\n{}\n".format(seq.name, seq.seq))
			else:
				result.write(">{}\n{}\n".format(seq.name, seq.seq))


def main():
	print("This script removes sequences that are too short in an alignment based on a percentage threshold.")

	parser = argparse.ArgumentParser(description='How to use argparse')
	parser.add_argument('-f', '--fastain', help='Fasta/Phylip set to be trimmed', required=True)
	parser.add_argument('-t', '--threshold', help='Threshold for omission', required=True)
	parser.add_argument('-m', '--metadata', help='Metadata file', default="")
	args = parser.parse_args()

	#FORREST creates a three-column table suitable for this:
	if args.metadata != "":
		coverage_d = coverage(args.metadata)
	else:
		extension = args.fastain.split(".")[-1]
		if extension in ("fasta", "fas", "fst", "fa", "faa", "fna", "ali", "aln"):
			fileformat = "fasta"
		elif extension in ("phy", "phylip"):
			fileformat = "phylip-relaxed"
		else:
			quit("Could not identify infile format:{}\nIs it FASTA/PHYLIP?".format(extension))
		coverage_d = coverage_from_alignment(args.fastain, fileformat)

	filter_alignment(args.fastain, float(args.threshold), coverage_d)


if __name__ == '__main__':
	main()
