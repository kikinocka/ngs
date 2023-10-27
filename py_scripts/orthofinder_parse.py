#!/usr/bin/env python3
import os
import pandas as pd


# os.chdir('/Users/kika/ownCloud/archamoebae/orthofinder/')
# table = open('Orthogroups.tsv')

# og_dict = {}
# for line in table:
# 	og = line.split('\t')[0]
# 	acc = line.strip().split('\t')[1:]
# 	og_dict[og] = acc

# with open('Orthogroups_upd.tsv', 'w') as out:
# 	for key, value in og_dict.items():
# 		for i in value:
# 			out.write('{}\t{}\n'.format(key, i))


os.chdir('/Users/kika/ownCloud/blasto_comparative/no_stop_proteins/OGs/')
table = pd.read_table('B.tsv')
headers = list(table.columns)[1:]
# headers = [item.replace('Ch. caulleryi', 'Chilomastixcau').replace('Ch. cuspidata', 'Chilomastixcus') for item in headers]
# print(headers)

OGs = ['OG0000025', 'OG0000035', 'OG0000050', 'OG0000053', 'OG0004267']

rows = []
for index, row in table.iterrows():
	if row[0] in OGs:
		rows.append(row.tolist())
	else:
		pass
# print(rows)

for row in rows:
	fname = row[0]
	row = row[1:]
	combz = zip(headers, row)
	combd = dict(combz)
	print(fname)
	# print(row)
	# print(combd)

	for key, value in combd.items():
		# print(key)
		# print(value)
		if os.path.isdir('{}'.format(fname)) == True:
			pass
		else:
			os.mkdir('{}'.format(fname))
		if isinstance(value, str) == False:
			pass
		else:
			with open('{}/{}.txt'.format(fname, key), 'w') as out:
				out.write('{}\n'.format(value.replace(', ', '\n')))
