#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/media/4TB1/blastocrithidia/orthofinder/other_ogs/stops_replaced/')
files = os.listdir()
moved = open('two_prot.txt', 'w')

count = 0
for file in files:
	if file.endswith('.fa') :
		for seq in SeqIO.parse(file, 'fasta'):
			count += 1
		print('{}\t{}'.format(file, count))
		if count == 2:
			moved.write(file + '\n')
			os.rename('{}'.format(file), 'two_prot/{}'.format(file))
		else:
			pass
		count = 0
