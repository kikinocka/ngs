#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/manuscripts/33_oil_sands-mtDNA/graphs/')
table = open('V9_all.tsv')

groups = {}
for line in table:
	if line.startswith('OTU'):
		headers = line
	elif 'No_hit' in line.split('\t')[48]: #check position of taxonomy assignment in the table
		if 'No_hit' not in groups:
			groups['No_hit'] = [line]
		else:
			groups['No_hit'].append(line)
	else:
		group = line.split('\t')[48].split('|')[1] #check position of taxonomy assignment in the table
		if group not in groups:
			groups[group] = [line]
		else:
			groups[group].append(line)


for key, value in groups.items():
	with open('V9_{}.tsv'.format(key), 'w') as out:
		out.write(headers)
		for item in value:
			out.write(item)
