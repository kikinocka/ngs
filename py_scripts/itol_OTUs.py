import argparse
import re
from math import log

def parse_colors(infile, sep="\t"):
	colors_d = {}
	for l in infile:
		l = l.strip().split(sep)
		colors_d[l[0]] = l[1]

	return colors_d


def write_itol(infile, outfile, colors_d, sep="\t"):
	size_re = r'size=(\d+)'
	scale_factor = 2

	with open(infile) as f,\
		 open(outfile, "wt") as result:
		result.write(header_symbols)
		for l in f:
			name = l.strip()
			color = colors_d.get(name, "#C72C48")
			size = re.search(size_re, name)
			if size: 
				size = size.group(1)
				size = int(2 + scale_factor*log(int(size), 2))
				result.write("{}\t2\t{}\t{}\t1\t1\n".format(name, size, color, ))
			else:
				size = 13
				pass #do not write reference taxa


def main():
	global header_symbols
	header_symbols = """DATASET_SYMBOL
SEPARATOR TAB
DATASET_LABEL	taxonomy
DATA
#First 3 fields define the node, shape and size
#Shape should be a number between 1 and 6, or any protein domain shape definition.
#1: square
#2: circle
#3: star
#4: right pointing triangle
#5: left pointing triangle
#6: checkmark
#next three are color, fill color, and position on branch - 1 is the tip
"""
	parser = argparse.ArgumentParser(description='How to use argparse')
	parser.add_argument('-i', '--infile', help='Sequences', default="metamonads_names.txt")
	parser.add_argument('-c', '--colors', help='Colors in tsv', default=None)

	args = parser.parse_args()
	suffix = args.infile.split(".")[-1]
	outfile = args.infile.replace(suffix, "itol.txt")
	if args.colors:
		colors_d = parse_colors(args.colors)
	else:
		colors_d = {}

	write_itol(args.infile, outfile, colors_d)


if __name__ == '__main__':
	main()