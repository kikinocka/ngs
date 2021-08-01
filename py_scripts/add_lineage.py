#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/SL_Euglenozoa/V9/')
table = open('otu_table.V9DS.tsv')

for line in table:
	if line.startswith('OTU'):
		print(line)
	# if line.split('\t')[22] == 'No_hit':
	# 	print(line)