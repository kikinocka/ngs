#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/storage/brno3-cerit/home/kika/sl_euglenozoa/v9/V9_DeepSea/decontaminated/stramenopiles/')
files = [x for x in os.listdir() if x.endswith('.fasta')]

for file in files:
	with open('{}_updated.fa'.format(file.split('.fasta')[0])) as out:
		for seq in SeqIO.parse(file, 'fasta'):
			out.write('>{}\n{}\n'.format(seq.description, (seq.seq).replace('.', '-').replace(' ', '')))
