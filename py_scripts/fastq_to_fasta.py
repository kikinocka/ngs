#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/blasto_reads/')

infile = SeqIO.parse('HR-05_2.fastq', 'fastq')
output = open('HR-05_2.fasta', 'w')

for sequence in infile:
	seq = sequence.seq
	name = sequence.description
	output.write('>{}\n{}\n'.format(name, seq))
output.close()
