#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/home/kika/MEGAsync/blasto_project/orthofinder/sg_ogs/jac_renamed/')
files = os.listdir()

counts = [0, 0, 0, 0]
for file in files:
	if file.endswith('.aln'):
		print(file)
		for seq in SeqIO.parse(file, 'fasta'):
			if 'Bp57' in seq.name:
				counts[0] += 1
			elif 'Btri' in seq.name:
				counts[1] += 1
			elif 'Bexl' in seq.name:
				counts[2] += 1
			elif 'Jac' in seq.name:
				counts[3] += 1

with open('gene_count.txt', 'w') as out:
	p57 = counts[0]
	triat = counts[1]
	bexlh = counts[2]
	jac = counts[3]
	out.write('p57:\t{}\ntriat:\t{}\nbexlh:\t{}\njac:\t{}\n'.format(p57, triat, bexlh, jac))
