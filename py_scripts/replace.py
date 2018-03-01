#!/usr/bin/python3
import os
import re
from Bio import SeqIO

os.chdir('/media/4TB1/blastocrithidia/orthofinder/other_ogs/')
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

# for file in files:
# 	if 'fa' in file:
# 		name = file.split('_replaced.fa')[0]
# 		print(name)
# 		proteins = SeqIO.parse(file, 'fasta')
# 		replaced = open('/home/kika/MEGAsync/blasto_project/orthofinder/sc_ogs/problems/new/{}_replaced2.fa'.format(name), 'w')
# 		notes = open('/home/kika/MEGAsync/blasto_project/orthofinder/sc_ogs/problems/{}_notes.txt'.format(name), 'w')
# 		for protein in proteins:
# 			if re.search(r'CDS_\d+', str(protein.seq)):
# 				replaced.write('>{}\n{}\n'.format(protein.description, re.sub(r'CDS_\d+', '', str(protein.seq))))
# 				notes.write('{}\t{}\n'.format(protein.name, re.search(r'CDS_\d+', str(protein.seq))))
# 			elif '+' in protein.seq:
# 				replaced.write('>{}\n{}\n'.format(protein.description, str(protein.seq).replace('+', 'X')))
# 				notes.write('{}\t{}\t{}\n'.format(protein.name, protein.seq.find('+'), '+'))
# 			elif '#' in protein.seq:
# 				replaced.write('>{}\n{}\n'.format(protein.description, str(protein.seq).replace('#', 'X')))
# 				notes.write('{}\t{}\t{}\n'.format(protein.name, protein.seq.find('#'), '#'))
# 			else:
# 				replaced.write('>{}\n{}\n'.format(protein.description, protein.seq))
