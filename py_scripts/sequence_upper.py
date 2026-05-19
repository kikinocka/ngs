#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/Downloads/')
infile = 'GCA_001766655.1_ASM176665v1_genomic.fna'
outfile = 'Pfra_genome.fna'

with open(outfile, 'w') as result:
	for seq in SeqIO.parse(infile, 'fasta'):
		result.write('>{}\n{}\n'.format(seq.description, seq.seq.upper()))
