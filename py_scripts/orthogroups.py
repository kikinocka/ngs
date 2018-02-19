#!/usr/bin/python3
# import os
from Bio import SeqIO

# os.chdir('/home/kika/MEGAsync/blasto_project/orthofinder/')
single = open('/media/4TB1/blastocrithidia/orthofinder/Results_Jan03/WorkingDirectory/SingleCopyOrthogroups_2.txt')
OGs = open('/media/4TB1/blastocrithidia/orthofinder/Results_Jan03/WorkingDirectory/Orthogroups_2.txt')

scOG = []
for line in single:
	scOG.append(line[:-1])

names = {}
for OG in OGs:
	names[OG.split(': ')[0]] = OG.split(': ')[1].replace(' ', ', ').replace('\n', '')

single_copy = {}
others = {}
for key, value in names.items():
	if key in scOG:
		single_copy[key] = value
	else:
		others[key] = value

for key, value in single_copy.items():
	out_single = open('/media/4TB1/blastocrithidia/orthofinder/sc_ogs/{}.fa'.format(key), 'w')
	for sequence in SeqIO.parse('/media/4TB1/blastocrithidia/orthofinder/all.fa', 'fasta'):
		for i in value.split(', '):
			if sequence.name == i:
				print('{}_____single_____{}'.format(i, key))
				out_single.write('>{}\n{}\n'.format(sequence.description, sequence.seq))

for key, value in others.items():
	out_others = open('/media/4TB1/blastocrithidia/orthofinder/other_ogs/{}.fa'.format(key), 'w')
	for sequence in SeqIO.parse('/media/4TB1/blastocrithidia/orthofinder/all.fa', 'fasta'):
		for i in value.split(', '):
			if sequence.name == i:
				print('{}_____other_____{}'.format(i, key))
				out_others.write('>{}\n{}\n'.format(sequence.description, sequence.seq))
