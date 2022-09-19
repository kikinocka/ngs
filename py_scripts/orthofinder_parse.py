#!/usr/bin/env python3
import os


os.chdir('/Users/kika/ownCloud/archamoebae/orthofinder/')
table = open('Orthogroups.tsv')

og_dict = {}
for line in table:
	og = line.split('\t')[0]
	acc = line.strip().split('\t')[1:]
	og_dict[og] = acc

with open('Orthogroups_upd.tsv', 'w') as out:
	for key, value in og_dict.items():
		for i in value:
			out.write('{}\t{}\n'.format(key, i))
