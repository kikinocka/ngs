#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/home/kika/ownCloud/SAGs/phylogenomics/')
files = [x for x in os.listdir() if x.endswith('fas')]

with open('D1_seqs.fa', 'w') as out:
	for file in files:
		print(file)
		name = file.split('_')[0]
		for seq in SeqIO.parse(file, 'fasta'):
			if seq.name == 'D1Redo':
				out.write('>{} {}\n{}\n'.format(name, seq.name, str(seq.seq).replace('-', '')))
