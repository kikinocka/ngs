#!/usr/bin/env python3
import os
from Bio import AlignIO

os.chdir('/media/4TB1/blastocrithidia/seqfire/apicomplexans_aln/')
files = sorted(os.listdir())

# #number of sequences
# print(len(alignment))


#number of positions
for file in files:
	if file.endswith('.aln'):
		print(file.get_alignment_length())
