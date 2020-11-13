#!/usr/bin/env python3
import os
import random
from Bio import SeqIO, AlignIO

os.chdir('/Users/kika/ownCloud/pelomyxa_schiedti/peroxisomes/mastig_lopit/orthofinder/OGs_sc_tran-supp/fasta/')
files = [x for x in os.listdir() if x.endswith('.fa')]

for file in files:
	print(file)
	fname = file.split('.')[0]
	# with open('{}_middle.fa'.format(fname), 'w') as result:
	for seq in SeqIO.parse(file, 'fasta'):
		print(len(seq))
		# start = random.randint(0, 12)
		# print(start)
		

			# result.write('>{}\n{}\n'.format(seq.name, seq.seq[len(seq.seq)-12:len(seq.seq)]))
			# result.write('>{}\n{}\n'.format(seq.name, seq.seq[1:13]))
			# result.write('>{}\n{}\n'.format(seq.name, seq.seq[int(round(len(seq.seq)/2, 0)):int(round(len(seq.seq)/2, 0))+12]))

