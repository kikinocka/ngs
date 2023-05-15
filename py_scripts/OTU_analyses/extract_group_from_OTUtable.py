#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/SL_Euglenozoa/V9/')
table = open('otu_table.V9DS.no_chimera.2+samples.only_euks.updated.tsv')

groups = {}
for line in table:
	if line.startswith('OTU'):
		headers = line
	elif 'No_hit' in line.split('\t')[22]: #check position of taxonomy assignment in the table
		if 'No_hit' not in groups:
			groups['No_hit'] = [line]
		else:
			groups['No_hit'].append(line)
	else:
		group = line.split('\t')[22].split('|')[1] #check position of taxonomy assignment in the table
		if group not in groups:
			groups[group] = [line]
		else:
			groups[group].append(line)


for key, value in groups.items():
	with open('supergroups/{}.tsv'.format(key), 'w') as out:
		out.write(headers)
		for item in value:
			out.write(item)
