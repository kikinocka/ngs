#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/media/4TB1/blastocrithidia/orthofinder/other_ogs/stops_replaced/')
files = os.listdir()
moved = open('one_prot_files_repl.txt', 'w')

count = 0
for file in files:
	if file.endswith('replaced.fa'):
		for seq in SeqIO.parse(file, 'fasta'):
			count += 1
		print('{}\t{}'.format(file, count))
		if count == 1:
			moved.write(file + '\n')
			os.rename('{}'.format(file), 'one_prot_only/{}'.format(file))
		else:
			pass
		count = 0
