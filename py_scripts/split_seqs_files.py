#!/usr/bin/env python3
import os
from Bio import SeqIO


os.chdir('/Users/kika/ownCloud/angomonas_SNAREs/queries/')

for seq in SeqIO.parse('qa.fa', 'fasta'):
	with open('{}.fa'.format(seq.name), 'w') as result:
		result.write('>{}\n{}\n'.format(seq.description, seq.seq))
