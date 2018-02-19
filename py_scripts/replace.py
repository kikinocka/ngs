#!/usr/bin/python3
import os
from Bio import SeqIO

os.chdir('/media/4TB1/blastocrithidia/orthofinder/sc_ogs/')
files = os.listdir()

for file in files:
	name = file.split('.fa')[0]
	proteins = SeqIO.parse(file, 'fasta')
	print(name)
	replaced = open('{}_replaced.fa'.format(name), 'w')
	notes = open('{}_notes.txt'.format(name), 'w')
	for protein in proteins:
		position = protein.seq.find('*')
		if position == -1:
			replaced.write('>{}\n{}\n'.format(protein.description, protein.seq))
		elif position == len(protein.seq) - 1:
			replaced.write('>{}\n{}\n'.format(protein.description, protein.seq[:-1]))
			notes.write('{}\tend\n'.format(protein.name))
		else:
			replaced.write('>{}\n{}\n'.format(protein.description, str(protein.seq).replace('*', 'X')))
			notes.write('{}\t{}\n'.format(protein.name, position+1))
