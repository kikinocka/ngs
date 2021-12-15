#!/usr/bin/python3
import argparse
from Bio import AlignIO

def apply_mask(alignment_full, maskdata):
	mask = maskdata[0].seq
	length_m = len(mask)
	length_f = alignment_full.get_alignment_length()
	if length_f != length_m:
		print("Mask length does not match with that of the alignment!", length_f, length_m)
	filt = alignment_full[:, :0] #has to be two ranges!
	for col in range(0,len(mask)):
		if col % 2500 == 0:
			print("processed: {}".format(col))
		if mask[col] != "-":
			#print(align[:, col:col+1]) #just col won't work
			filt += alignment_full[:, col:col+1]
	return filt

def find_format(suffix):
	accepted = ["fasta", "phylip", "clustal", "emboss", "nexus", "stockholm"]
	if suffix in accepted:
		return suffix
	elif suffix in ["fasta", "fna", "faa", "fas", "fa"]:
		return "fasta"
	elif suffix in ["ali", "aln"]:
		return "fasta" #probably
	elif suffix in ["phylip", "phy"]:
		return "phylip-relaxed"
	elif suffix in ["nexus", "nex"]:
		return "nexus"
	else:
		quit("unrecognized MSA format")

def find_trim_mask(alignment_full, alignment_trimmed):
	length_f, length_t = alignment_full.get_alignment_length(), alignment_trimmed.get_alignment_length()
	trim_mask = ""
	tpos = 0
	print("Processing alignment {} chars long".format(length_f))
	for pos in range(0, length_f):
		if pos % 2500 == 0:
			print("processed: {}".format(pos))
		try:
			if alignment_full[:, pos] == alignment_trimmed[:, tpos]:
				trim_mask += "X"
				tpos += 1
				if tpos == length_t:
					remaining = length_f - len(trim_mask) #+ 1
					trim_mask += remaining*"-"
					break
			else:
				trim_mask += "-"
		except IndexError:
			print(pos)
	print("length full: {}, length mask: {}".format(length_f, len(trim_mask)))
	return trim_mask

def main():
	print("Make a mask file using a --full_alignment file and a --trim_alignment file; or mask a --full_alignment file using a --mask file.")
	parser = argparse.ArgumentParser(description='How to use argparse')
	parser.add_argument('-f', '--full_alignment', help='Full alignment (fasta/phylip)', required=True)
	parser.add_argument('-o', '--outfile', help='Output filename', default="")
	group = parser.add_mutually_exclusive_group()
	group.add_argument('-t', '--trim_alignment', help='Trimmed alignment', default="")
	group.add_argument('-m', '--mask', help='Mask for input alignment', default="")

	args = parser.parse_args()

	infile_f = args.full_alignment
	suffix_f = infile_f.split(".")[-1]
	alignment_full = AlignIO.read(infile_f, find_format(suffix_f))

	if args.mask == "":
		if args.outfile == "":
			outfile = infile_f.replace(suffix_f, "mask.fasta")
		infile_t = args.trim_alignment
		suffix_t = infile_t.split(".")[-1]
		alignment_trimmed = AlignIO.read(infile_t, find_format(suffix_t))

		#check if alignment labels match
		labels_f = [x.id for x in alignment_full]
		labels_t = [x.id for x in alignment_trimmed]
		print("Labels matched:", labels_t == labels_f)

		mask = find_trim_mask(alignment_full, alignment_trimmed)
		with open(outfile, "wt") as result:
			result.write(">MASK\n{}\n".format(mask))

	else:
		if args.outfile == "":
				outfile = infile_f.replace(suffix_f, "masked.fasta")
		suffix_m = args.mask.split(".")[-1]
		alignment_mask = AlignIO.read(args.mask, find_format(suffix_m))
		trimmed = apply_mask(alignment_full, alignment_mask)
		with open(outfile, "wt") as result:
			AlignIO.write(trimmed, result, "fasta")


if __name__ == '__main__':
	main()
