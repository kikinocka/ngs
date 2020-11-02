#!/usr/bin/env python3
import os
import re
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/pelomyxa_schiedti/peroxisomes/mastig_lopit/')
infile = open('orthofinder/pelo_mastig_orthogroups.txt')
pelo_fa = SeqIO.parse('/Users/kika/ownCloud/pelomyxa_schiedti/blastdb/pelomyxa_predicted_proteins_corr.fa', 'fasta')
mast_fa = SeqIO.parse('mastig_lopit.fa', 'fasta')

mast_name = r'm51a1_g\d+'
pelo_name = r'Pelo\d+'

pelo_all = {}
mast_all = {}
for line in infile:
	og = line.split(' ')[0][:-1]
	# print(og)
	pelo = []
	for i in [(a.start(), a.end()) for a in list(re.finditer(pelo_name, line))]:
		pelo_num = line[i[0]:i[-1]]
		pelo.append(pelo_num)
	pelo_all[og] = pelo

	mast = []
	for i in [(a.start(), a.end()) for a in list(re.finditer(mast_name, line))]:
		mast_num = line[i[0]:i[-1]]
		mast.append(mast_num)
	mast_all[og] = mast


for seq in pelo_fa:
	for og, accessions in pelo_all.items():
		for pelo in accessions:
			if pelo == seq.name:
				with open('orthofinder/OGs/{}.fa'.format(og), 'a') as result:
					result.write('>{}\n{}\n'.format(pelo, seq.seq))


for seq in mast_fa:
	for og, accessions in mast_all.items():
		for mast in accessions:
			if mast == seq.name:
				with open('orthofinder/OGs/{}.fa'.format(og), 'a') as result:
					result.write('>{}\n{}\n'.format(mast, seq.seq))
