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
table = pd.read_table('J.tsv')
headers = list(table.columns)[1:]
# headers = [item.replace('Ch. caulleryi', 'Chilomastixcau').replace('Ch. cuspidata', 'Chilomastixcus') for item in headers]
# print(headers)

OGs = ['OG0000069', 'OG0000100', 'OG0000109', 'OG0000142', 'OG0000213', 'OG0000290', 'OG0000296', 'OG0000302', 'OG0000306', 'OG0000310', 'OG0000328', 'OG0000329', 'OG0000349', 'OG0000350', 'OG0000371', 'OG0000376', 'OG0000386', 'OG0000387', 'OG0000412', 'OG0000413', 'OG0000416', 'OG0000418', 'OG0000419', 'OG0000420', 'OG0000432', 'OG0000435', 'OG0000438', 'OG0000445', 'OG0000447', 'OG0000448', 'OG0000449', 'OG0000461', 'OG0000468', 'OG0000470', 'OG0000471', 'OG0000474', 'OG0000475', 'OG0000479', 'OG0000481', 'OG0000483', 'OG0000486', 'OG0000487', 'OG0000488', 'OG0000502', 'OG0000503', 'OG0000507', 'OG0000516', 'OG0000531', 'OG0000532', 'OG0000542', 'OG0000578', 'OG0000589', 'OG0000592', 'OG0000593', 'OG0000600', 'OG0000612', 'OG0000623', 'OG0000632', 'OG0000637', 'OG0000673', 'OG0000704', 'OG0000708', 'OG0000807', 'OG0000809', 'OG0000931', 'OG0001551', 'OG0004742', 'OG0005673', 'OG0008731', 'OG0009363']

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
