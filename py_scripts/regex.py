#!/usr/bin/python3
from Bio import SeqIO
import re

infile = SeqIO.parse('/home/kika/scripts/ngs/reads.fq', 'fastq')
fw_out = open('/home/kika/scripts/ngs/reads_fw.fq', 'w')
rev_out = open('/home/kika/scripts/ngs/reads_rev.fq', 'w')

# for sequence in infile:
# 	print(sequence.name)
# 	sequence.name = re.sub('_\d+\Z', '', sequence.name)
# 	print(sequence.name)


# header = '@SRR1186295.1.1 1 length=100'

for read in infile:
	if re.search('SRR\d+.\d.1 ', read.description):
		fw_out.write(read.format('fastq'))
	elif re.search('SRR\d+.\d.2 ', read.description):
		rev_out.write(read.format('fastq'))
	else:
		print(read.description)