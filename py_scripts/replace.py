#!/usr/bin/python3
import os
import re
from Bio import SeqIO

os.chdir('/media/4TB1/blastocrithidia/orthofinder/other_ogs/stops_replaced/')
files = os.listdir()

# for file in files:
# 	if file.endswith('.fa'):
# 		name = file.split('.fa')[0]
# 		proteins = SeqIO.parse(file, 'fasta')
# 		print(name)
# 		replaced = open('stops_replaced/{}_replaced.fa'.format(name), 'w')
# 		notes = open('stops_replaced/notes.txt'.format(name), 'a')
# 		for protein in proteins:
# 			position = protein.seq.find('*')
# 			if position == -1:
# 				replaced.write('>{}\n{}\n'.format(protein.description, protein.seq))
# 			elif position == len(protein.seq) - 1:
# 				replaced.write('>{}\n{}\n'.format(protein.description, protein.seq[:-1]))
# 				notes.write('{}\t{}\tend\n'.format(name, protein.name))
# 			else:
# 				replaced.write('>{}\n{}\n'.format(protein.description, str(protein.seq).replace('*', 'X')))
# 				notes.write('{}\t{}\t{}\n'.format(name, protein.name, position+1))

for file in files:
	if file.endswith('_replaced.fa'):
		name = file.split('_')[0]
		print(name)
		proteins = SeqIO.parse(file, 'fasta')
		replaced = open('{}_replaced2.fa'.format(name), 'w')
		notes = open('notes2.txt'.format(name), 'a')
		for protein in proteins:
			if re.search(r'CDS_\d+', str(protein.seq)):
				replaced.write('>{}\n{}\n'.format(protein.description, re.sub(r'CDS_\d+', '', str(protein.seq))))
				notes.write('{}\t{}\t{}\n'.format(name, protein.name, re.search(r'CDS_\d+', str(protein.seq))))
			elif '+' in protein.seq:
				replaced.write('>{}\n{}\n'.format(protein.description, str(protein.seq).replace('+', 'X')))
				notes.write('{}\t{}\t{}\t{}\n'.format(name, protein.name, protein.seq.find('+')+1, '+'))
			elif '#' in protein.seq:
				replaced.write('>{}\n{}\n'.format(protein.description, str(protein.seq).replace('#', 'X')))
				notes.write('{}\t{}\t{}\t{}\n'.format(name, protein.name, protein.seq.find('#')+1, '#'))
			else:
				replaced.write('>{}\n{}\n'.format(protein.description, protein.seq))
