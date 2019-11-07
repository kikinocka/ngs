#!/usr/bin/env python3

import os

os.chdir('/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Tetrapyrroles/precorrin-2_dehydrogenase/')
table = open('bct_SDR_a4.presence.tsv')

all = {}
for line in table:
	if line.split('\t')[0] in all:
		print(line)
	else:
		all[line.split('\t')[0]] = line.split('\t')[1:3]

with open('bct_SDR_a4.presence_dedupl.tsv', 'w') as result:
	for key, value in all.items():
		result.write('{}\t{}\t{}'.format(key, value[0], value[1]))
