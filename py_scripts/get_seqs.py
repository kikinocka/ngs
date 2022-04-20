#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/blastocrithidia/genes/tRNAs/ciliates/')
files = [x for x in os.listdir() if x.endswith('aragorn.fa')]

with open('Trp-tRNAs.fa', 'w') as out:
	for file in files:
		print(file)
		name = '{}_{}'.format(file.split('_')[0], file.split('_')[1])
		c = 0
		for seq in SeqIO.parse(file, 'fasta'):
			if 'Trp' in seq.name:
				c += 1
				out.write('>{} {}\n{}\n'.format(name, seq.description, seq.seq))
		print(c)