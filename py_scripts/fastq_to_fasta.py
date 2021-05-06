#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/storage/brno3-cerit/home/kika/oil_sands/metagenome/reads/')

infile = SeqIO.parse('BML_trimmed_1.fq', 'fastq')
output = open('BML_trimmed_1.fa', 'w')

for sequence in infile:
	seq = sequence.seq
	name = sequence.name
	output.write('>{}\n{}\n'.format(name, seq))
output.close()
