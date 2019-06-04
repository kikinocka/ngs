#!/usr/bin/env python3
import os
from Bio import SeqIO
from collections import OrderedDict

os.chdir('/home/kika/Dropbox/orthoMCL_kika/orthofasta/')
files = [x for x in os.listdir() if x.endswith('.fas')]

with open('EG_missing-in-EL.fa', 'w') as result:
	print('Searching for files without EL')
	names = []
	for file in files:
		print(file)
		if '>DEEL' not in open(file).read():
			names.append(file)
	
	print('Searching for EG sequences')
	for file in files:
		if file in names:
			print(file)
			n = file.split('.')[0]
			for seq in SeqIO.parse(file, 'fasta'):
				if 'DEEG' in seq.description:
					result.write('>{}\t{}\n{}\n'.format(seq.description, n, seq.seq))
