#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/oil_sands/amplicons/V4-sediment')
table = open('otu_table.tsv')

groups = {}
for line in table:
	if line.startswith('OTU'):
		headers = line
	elif 'No_hit' in line.split('\t')[10]:
		if 'No_hit' not in groups:
			groups['No_hit'] = [line]
		else:
			groups['No_hit'].append(line)
	else:
		group = line.split('\t')[10].split('|')[1]
		if group not in groups:
			groups[group] = [line]
		else:
			groups[group].append(line)


for key, value in groups.items():
	with open('{}.tsv'.format(key), 'w') as out:
		out.write(headers)
		for item in value:
			out.write(item)
