#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/media/4TB1/blastocrithidia/api_NOG/apiNOG_raw_algs_single/')
files = os.listdir()
moved = open('one_prot.txt', 'w')

count = 0
for file in files:
	if file.endswith('.fa') :
		for seq in SeqIO.parse(file, 'fasta'):
			count += 1
		print('{}\t{}'.format(file, count))
		if count == 2:
			moved.write(file + '\n')
			os.rename('{}'.format(file), 'one_prot/{}'.format(file))
		else:
			pass
		count = 0
