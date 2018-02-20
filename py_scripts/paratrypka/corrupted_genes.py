#!/usr/bin/python3
import os

os.chdir('/home/kika/paratrypanosoma/')
names = open('corrupted_genes.txt', 'r')
gff = open('result_renamed_lengths_no_split.gff', 'r')
out = open('corrupted_genes_both_names.tsv', 'w')

names_list = []
for line in names:
	names_list.append(line[:-1])

both = {}
for row in gff:
	if row.startswith('##'):
		pass
	else:
		pcon = row.split('\t')[8].split('ID=')[1].split(';')[0]
		old = row.split('\t')[8].split('ID=')[1].split(';')[1].split('Note=')[1][:-1]
		both[pcon] = old

for key, value in both.items():
	if key in names_list:
		out.write('{}\t{}\n'.format(key, value))
out.close()