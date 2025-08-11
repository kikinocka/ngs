#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/membrane-trafficking/ARFs_ASR/Alignment/')
files = [x for x in os.listdir() if x.endswith('.fa')]

with open('Arf1_final.tsv', 'w') as result:
	for file in files:
		print(file)
		fname = file.split('.')[0]
		# with open('{}_middle.fa'.format(fname), 'w') as result:
		result.write('{}\n'.format(fname))
		for seq in SeqIO.parse(file, 'fasta'):
			result.write('{}\t{}\n'.format(seq.name, seq.seq[len(seq.seq)-5:len(seq.seq)]))
			# result.write('>{}\n{}\n'.format(seq.name, seq.seq[len(seq.seq)-12:len(seq.seq)]))
			# result.write('>{}\n{}\n'.format(seq.name, seq.seq[1:13]))
			# result.write('>{}\n{}\n'.format(seq.name, seq.seq[int(round(len(seq.seq)/2, 0)):int(round(len(seq.seq)/2, 0))+12]))
		result.write('\n')

