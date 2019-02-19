#!/usr/bin/env python3
import os
from Bio import AlignIO

os.chdir('/home/kika/ownCloud/blastocrithidia/seqfire/apicomplexans/')
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
