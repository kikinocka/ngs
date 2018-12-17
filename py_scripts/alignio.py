#!/usr/bin/env python3
import os
from Bio import AlignIO

os.chdir('/media/4TB1/blastocrithidia/seqfire/apicomplexans_aln/')
files = sorted(os.listdir())
out = open('aln_len.tsv', 'w')

# #number of sequences
# print(len(alignment))


for file in files:
	if file.endswith('.aln'):
		name = file.split('.')[0]
		aln = AlignIO.read(file, 'fasta')
		#number of positions
		out.write('{}\t{}\n'.format(name, aln.get_alignment_length()))

out.close()
