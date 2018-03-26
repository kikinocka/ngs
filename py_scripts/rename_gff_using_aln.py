#!/usr/bin/env python3
from Bio import SeqIO
import os

os.chdir('/home/kika/MEGAsync/blasto_project/orthofinder/sg_ogs/jac_renamed/')
files = os.listdir()
gff = open('jac_insertions.gff')

names = {}
for file in files:
	if file.endswith('.aln'):
		print(file)
		for sequence in SeqIO.parse(file, 'fasta'):
			if 'Jac' in sequence.name:
				names[sequence.name.split('_')[1]] = sequence.description.split(' ')[1]

with open('jac_insertions_renamed.gff', 'w') as out:
	for line in gff:
		if line.split('\t')[0] in names.keys():
			new_line = line.replace(line.split('\t')[0], names[line.split('\t')[0]])
			out.write(new_line)
