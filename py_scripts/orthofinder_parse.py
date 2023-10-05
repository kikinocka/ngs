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


os.chdir('/Users/kika/ownCloud/blasto_comparative/Results_Oct02/blasto-specific/')
table = pd.read_table('blasto-spec_OGs.tsv')
headers = list(table.columns)[1:]
# headers = [item.replace('Ch. caulleryi', 'Chilomastixcau').replace('Ch. cuspidata', 'Chilomastixcus') for item in headers]
# print(headers)

OGs = ['OG0000135', 'OG0000714', 'OG0005005', 'OG0006144', 'OG0006426', 'OG0006797', 'OG0006802', 'OG0006973', 'OG0006976', 'OG0007113', 'OG0007125', 'OG0007128', 'OG0007133', 'OG0007135', 'OG0007276', 'OG0007279', 'OG0007282', 'OG0007285', 'OG0007290', 'OG0007291', 'OG0007294', 'OG0007299', 'OG0007304', 'OG0007306', 'OG0007431', 'OG0007435', 'OG0007437', 'OG0007439', 'OG0007440', 'OG0007445', 'OG0007446', 'OG0007447', 'OG0007449', 'OG0007451', 'OG0007455', 'OG0007457', 'OG0007459', 'OG0007460', 'OG0007464', 'OG0007469', 'OG0007470', 'OG0007473', 'OG0007475', 'OG0007476', 'OG0007477', 'OG0007478', 'OG0007481', 'OG0007482', 'OG0007483', 'OG0007484', 'OG0007729', 'OG0007731', 'OG0007734', 'OG0007735', 'OG0007738', 'OG0007740', 'OG0007741', 'OG0007742', 'OG0007743', 'OG0007744', 'OG0007745', 'OG0007749', 'OG0007754', 'OG0007756', 'OG0007758', 'OG0007759', 'OG0007761', 'OG0007762', 'OG0007764', 'OG0007766', 'OG0007767', 'OG0007770', 'OG0007771', 'OG0007773', 'OG0007775', 'OG0007776', 'OG0007777', 'OG0007778', 'OG0007779', 'OG0007785', 'OG0007787', 'OG0007788', 'OG0007789', 'OG0007972', 'OG0007973', 'OG0007974', 'OG0007976', 'OG0007977', 'OG0007978', 'OG0007979', 'OG0007980', 'OG0007981', 'OG0007982', 'OG0007983', 'OG0007984', 'OG0007986', 'OG0007987', 'OG0007988', 'OG0007989', 'OG0007990', 'OG0007991', 'OG0007992', 'OG0007993', 'OG0007994', 'OG0007996', 'OG0007997', 'OG0007998', 'OG0007999', 'OG0008000', 'OG0008001', 'OG0008002', 'OG0008003', 'OG0008004', 'OG0008005', 'OG0008006', 'OG0008008', 'OG0008009', 'OG0008010', 'OG0008011', 'OG0008012', 'OG0008013', 'OG0008014', 'OG0008016', 'OG0008017', 'OG0008018', 'OG0008019', 'OG0008020', 'OG0008021', 'OG0008022', 'OG0008023', 'OG0008024', 'OG0008026', 'OG0008027', 'OG0008028', 'OG0008029', 'OG0008030', 'OG0008031', 'OG0008032', 'OG0008033', 'OG0008034', 'OG0008036', 'OG0008037', 'OG0008038', 'OG0008039', 'OG0008041', 'OG0008043', 'OG0008044', 'OG0008045', 'OG0008046', 'OG0008047', 'OG0008048', 'OG0008049', 'OG0008050', 'OG0008051', 'OG0008052', 'OG0008053', 'OG0008055', 'OG0008056', 'OG0008058', 'OG0008059', 'OG0008060', 'OG0008061', 'OG0008062', 'OG0008064', 'OG0008065', 'OG0008067', 'OG0008068', 'OG0008069', 'OG0008070', 'OG0008071', 'OG0008292', 'OG0008293', 'OG0008294', 'OG0008295', 'OG0008296', 'OG0008297', 'OG0008298', 'OG0008299', 'OG0008300', 'OG0008301', 'OG0008303', 'OG0008305', 'OG0008306', 'OG0008308', 'OG0008310', 'OG0008311', 'OG0008314', 'OG0008315', 'OG0008316', 'OG0008317', 'OG0008319', 'OG0008323', 'OG0008327', 'OG0008329', 'OG0008330', 'OG0008331', 'OG0008332', 'OG0008336', 'OG0008338', 'OG0008342']

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
