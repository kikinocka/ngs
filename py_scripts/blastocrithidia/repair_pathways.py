#!/usr/bin/env python3
import os
from collections import OrderedDict

os.chdir('/home/kika/MEGAsync/blasto_project/ku_story/repair/')
files = os.listdir()
species = open('species.txt')

spp = OrderedDict()
for line in species:
	spp[line.split('\t')[0]] = (line.split('\t')[1], line.split('\t')[2][:-1])

for file in files:
	if file.endswith('.tsv'):
		print(file)
		file_name = file.split('_')[0]
		out = open('results/{}.tsv'.format(file_name), 'w')
		spp_ids = []
		for line in open(file):
			spp_ids.append(line.split('\t')[3])
		spp_ids = set(spp_ids)
		for key, value in spp.items():
			if key in spp_ids:
				out.write('{}\t{}\t1\n'.format(key, value[0]))
			else:
				out.write('{}\t{}\t0\n'.format(key, value[0]))
