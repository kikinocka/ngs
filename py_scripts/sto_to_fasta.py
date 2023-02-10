#!/usr/bin/env python3
import os
from Bio import AlignIO

os.chdir('/Users/kika/programs/tRNAscan-SE_CM_alignments/isotype_specific/Eukaryota/')
stockholms = [x for x in os.listdir() if x.endswith('.sto')]

for stockholm in stockholms:
	print(stockholm)
	name = stockholm.split('.sto')[0]
	record = AlignIO.parse(stockholm, 'stockholm')
	with open('{}.aln'.format(name), 'w') as result:
		AlignIO.write(record, result, 'fasta')
