#!/usr/bin/env python3
import os
from collections import defaultdict

os.chdir('/home/kika/MEGAsync/diplonema_mt/1610/')
contigs = open('contigs.txt')
blast = open('consensus_seqs_blast.tsv')

cont_list = []
for line in contigs:
	cont_list.append(line[:-1])

new_contigs = defaultdict(set)
for line in blast:
	try:
		query = line.split('\t')[0][0]
		subject = line.split('\t')[2]
		evalue = float(line.split('\t')[5])
		if evalue < float(1e-50):
			cont_list.append(subject)
			new_contigs[query].add(subject)
	except:
		pass

for key, value in new_contigs.items():
	print(key, value)
