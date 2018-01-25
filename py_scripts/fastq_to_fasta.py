#!/usr/bin/python3
from Bio import SeqIO

infile = SeqIO.parse('/home/kika/programs/blast-2.5.0+/bin/triat_raw_reads.fastq', 'fastq')
output = open('/home/kika/programs/blast-2.5.0+/bin/triat_raw_reads.fasta', 'w')

for sequence in infile:
	seq = sequence.seq
	name = sequence.name
	output.write('>{}\n{}\n'.format(name, seq))
output.close()