#!/usr/bin/env python3
import os
from Bio import AlignIO

os.chdir('/Users/kika/ownCloud/Gln-tRNA/manual_alns/')
alignments = [x for x in os.listdir() if x.endswith('.aln')]

for aln in alignments:
	print(aln)
	name = aln.split('.aln')[0]
	record = AlignIO.parse(aln, 'fasta')
	with open('{}.sto'.format(name), 'w') as result:
		AlignIO.write(record, result, 'stockholm')
