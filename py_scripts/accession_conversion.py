#!/usr/bin/env python3
import os
from collections import defaultdict

os.chdir('/Users/kika/ownCloud/diplonema/ms_data/')
accessions = open('accessions.tsv')

acc = defaultdict(list)
for line in accessions:
	if line.split('\t')[0] not in acc:
		acc[line.split('\t')[0]] = [line.strip().split('\t')[1]]
	else:
		acc[line.split('\t')[0]].append(line.strip().split('\t')[1])

with open('accessions_joined.tsv', 'w') as out:
	for key, value in acc.items():
		# print(key)
		out.write('{}\t'.format(key))
		for v in value:
			# print(v)
			out.write('{};'.format(v))
		out.write('\n')
