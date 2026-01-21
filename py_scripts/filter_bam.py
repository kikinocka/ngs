#!/usr/bin/python3

#courtesy of github.com/morpholino

import math
import pysam
import re
import sys
from pathlib import Path

# Including a low complexity filter
# Count words in sequence before assessing complexity
def count_words(sequence, wordsize):
	count = {}
	for i in range(0,len(sequence)-wordsize+1,1):
		string = sequence[i:i+wordsize]
		if string not in count:
			count[string] = 1
		else:
			count[string] += 1
	#print(count)
	return count

# Two ways of calculating complexity; here using cm
#https://academic.oup.com/nar/article/42/12/e99/1097867
#according to SeqComplex.pl
def cm(sequence, wordsize):
	length  = len(sequence)
	cm = 0
	m = 4**wordsize
	elements = count_words(sequence, wordsize)
	dw = float(length - wordsize + 1)
	for e in elements:
		if elements[e] > 0:
			try:
				r = elements[e] / dw
				cm -= r * math.log(r) / math.log(m)
			except ValueError:
				print("Could not process r:", elements[e], dw, r)
				quit()
	return cm

def ct(sequence, wordsize):
	length  = len(sequence)
	ct = 1
	for l in range(1, wordsize+1):
		vl = 0
		pot = 4**l
		vm = min(pot, length - l + 1)
		elements = count_words(sequence, l)
		for e in elements:
			if elements[e] > 0:
				vl += 1
		ct *= vl/vm
	return ct


# Thresholds (can later be made argparse arguments if desired)
READ_LENGTH_THRESHOLD = 75.0  # 75 in the first round
COV_THRESHOLD = 80.0

# BAM flag filters to exclude:
# 0x200: failed vendor quality checks
# 0x400: PCR/optical duplicate
# 0x800: supplementary alignment
EXCLUDE_FLAGS = 0x200 | 0x400 | 0x800


def calculate_query_coverage(aln):
	# Get CIGAR info: list of (operation, length)
	# M = 0, I = 1, D = 2, N = 3, S = 4, H = 5, P = 6, = = 7, X = 8, B = 9
	total_query_len = 0
	aligned_len = 0

	for op, length in aln.cigartuples:
		if op in {0, 4}:  # M (aligned), S (soft-clipped)
			total_query_len += length
		if op == 0:  # M only
			aligned_len += length

	if total_query_len == 0:
		return 0.0
	return aligned_len, total_query_len


def extract_aligned_sequence(read: pysam.AlignedSegment) -> str:
    """
    Extract the aligned portion of a read's sequence based on its CIGAR string.
    Ignores insertions (I=1), deletions (D=2), skips (N=3), soft clipping (S=4), and hard clipping (H=5).
    M = 0, I = 1, D = 2, N = 3, S = 4, H = 5, P = 6, = = 7, X = 8, B = 9
    """
    seq = read.query_sequence
    cigar = read.cigartuples  # list of (operation, length)
    if cigar is None or seq is None:
        return ""

    aligned_seq = []
    seq_pos = 0

    for op, length in cigar:
        if op in {0, 7, 8}:  # M, =, X
            aligned_seq.append(seq[seq_pos:seq_pos + length])
            seq_pos += length
        elif op in {1, 4, 5}:  # I, S, H
            seq_pos += length
        elif op in {2, 3}:  # D, N (ref-only ops)
            # don't advance seq_pos, nothing to consume in read
            continue

    return "".join(aligned_seq)


def analyze_bam(infile):
	"""Parse a BAM file, print alignment metrics, and write passing reads."""
	infile = Path(infile)
	outfile = infile.with_name(infile.stem + ".pass" + infile.suffix)

	try:
		samfile = pysam.AlignmentFile(str(infile), "rb")
		out_bam = pysam.AlignmentFile(str(outfile), "wb", header=samfile.header)
	except Exception as e:
		sys.exit(f"Failed to open BAM file: {e}")

	print("ReadId\tTarget\tpIdent\tReadCov\tReadLen")

	for read in samfile.fetch(until_eof=True):
		if read.is_unmapped:
			#print(read.query_name, "unmapped", read.flag)
			continue

		if read.flag & EXCLUDE_FLAGS:
			#print(read.query_name, "bad flag", read.flag)
			continue

		read_id = read.query_name
		target = read.reference_name
		genome = "" #target.split("|")[0]
		readseq = read.query_sequence
		matchingseq = extract_aligned_sequence(read)
		aligned_length, read_length = calculate_query_coverage(read)

		if read_length < READ_LENGTH_THRESHOLD:
			continue

		read_coverage = (aligned_length / read_length) * 100
		if read_coverage < COV_THRESHOLD:
			continue
		
		complexity_di = cm(matchingseq, 2)
		if complexity_di < 0.65:
			continue

		complexity_tri = cm(matchingseq, 3)
		if complexity_tri < 0.55:
			continue

		complexity_tetra = cm(matchingseq, 4)
		if complexity_tetra < 0.55:
			continue
			
		complexity_hexa = cm(matchingseq, 6)
		if complexity_hexa < 0.50:
			continue
		
		# Visually check the complexity of various k-mers
		#print(f"{matchingseq}: {complexity_di:.2f}, {complexity_tri:.2f}, {complexity_tetra:.2f}, {complexity_hexa:.2f}")
			
		# Write read if passed the above filters
		out_bam.write(read)

		# Counting matching bases from CIGAR does not work; 
		# CIGAR only describes clipped/matching regions of the read
		#matches = sum(length for op, length in read.cigartuples if op == 0)

		# Determine matches from the number of mismatches (NM tag)
		try:
			nm = read.get_tag("NM")
			matches = aligned_length - nm
		except KeyError:
			nm = "NA"
			matches = 0

		percent_identity = (matches / aligned_length) * 100 if aligned_length > 0 else 0

		# Output result
		if False:
			print(
				f"{read_id}\t{genome}\t"
				f"{percent_identity:.2f}\t"
				f"{read_coverage:.2f}\t"
				f"{read_length}"
			)


	samfile.close()
	out_bam.close()
	print(f"Passing reads written to {outfile}")


def main():
	if len(sys.argv) < 2:
		sys.exit(f"Usage: {sys.argv[0]} file.bam\nError: No filename provided!")

	infile = sys.argv[1]
	analyze_bam(infile)


if __name__ == "__main__":
	main()
