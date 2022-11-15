#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/SL_Euglenozoa/V9/')
table = open('otu_table.V9DS_updated.no_chimera.tsv')
result = open('otu_table.V9DS_updated.no_chimera.2samples.tsv', 'w')
error = open('otu_table.V9DS_updated.no_chimera.1sample.tsv', 'w')


for line in table:
	count = list()
	for value in line.split('\t')[2:18]:
		if value == str(0):
			pass
		else:
			count.append(value)
	if len(count) > 1:
		result.write(line)
	else:
		error.write(line)
