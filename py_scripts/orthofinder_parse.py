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


os.chdir('/Users/kika/ownCloud/blasto_comparative/orthofinder_Aug18/blasto-specific/')
table = pd.read_table('blasto-specificOGs.tsv')
headers = list(table.columns)[1:]
# headers = [item.replace('Ch. caulleryi', 'Chilomastixcau').replace('Ch. cuspidata', 'Chilomastixcus') for item in headers]
# print(headers)

OGs = ['OG0000137', 'OG0000714', 'OG0005005', 'OG0006143', 'OG0006425', 'OG0006615', 'OG0006800', 'OG0006971', 'OG0006974', 'OG0007110', 'OG0007122', 'OG0007125', 'OG0007130', 'OG0007132', 'OG0007273', 'OG0007276', 'OG0007279', 'OG0007282', 'OG0007287', 'OG0007288', 'OG0007291', 'OG0007296', 'OG0007301', 'OG0007303', 'OG0007429', 'OG0007433', 'OG0007435', 'OG0007437', 'OG0007438', 'OG0007443', 'OG0007444', 'OG0007445', 'OG0007447', 'OG0007449', 'OG0007453', 'OG0007455', 'OG0007457', 'OG0007458', 'OG0007462', 'OG0007467', 'OG0007468', 'OG0007471', 'OG0007473', 'OG0007474', 'OG0007475', 'OG0007476', 'OG0007479', 'OG0007480', 'OG0007481', 'OG0007482', 'OG0007727', 'OG0007729', 'OG0007732', 'OG0007733', 'OG0007736', 'OG0007738', 'OG0007739', 'OG0007740', 'OG0007741', 'OG0007742', 'OG0007743', 'OG0007747', 'OG0007752', 'OG0007754', 'OG0007756', 'OG0007757', 'OG0007759', 'OG0007760', 'OG0007762', 'OG0007764', 'OG0007765', 'OG0007768', 'OG0007769', 'OG0007771', 'OG0007773', 'OG0007774', 'OG0007775', 'OG0007776', 'OG0007777', 'OG0007783', 'OG0007785', 'OG0007786', 'OG0007787', 'OG0007971', 'OG0007972', 'OG0007973', 'OG0007975', 'OG0007976', 'OG0007977', 'OG0007978', 'OG0007979', 'OG0007980', 'OG0007981', 'OG0007982', 'OG0007983', 'OG0007985', 'OG0007986', 'OG0007987', 'OG0007988', 'OG0007989', 'OG0007990', 'OG0007991', 'OG0007992', 'OG0007993', 'OG0007995', 'OG0007996', 'OG0007997', 'OG0007998', 'OG0007999', 'OG0008000', 'OG0008001', 'OG0008002', 'OG0008003', 'OG0008004', 'OG0008005', 'OG0008007', 'OG0008008', 'OG0008009', 'OG0008010', 'OG0008011', 'OG0008012', 'OG0008013', 'OG0008015', 'OG0008016', 'OG0008017', 'OG0008018', 'OG0008019', 'OG0008020', 'OG0008021', 'OG0008022', 'OG0008024', 'OG0008025', 'OG0008026', 'OG0008027', 'OG0008028', 'OG0008029', 'OG0008030', 'OG0008031', 'OG0008032', 'OG0008034', 'OG0008035', 'OG0008036', 'OG0008037', 'OG0008039', 'OG0008041', 'OG0008042', 'OG0008043', 'OG0008044', 'OG0008045', 'OG0008046', 'OG0008047', 'OG0008048', 'OG0008049', 'OG0008050', 'OG0008051', 'OG0008053', 'OG0008054', 'OG0008056', 'OG0008057', 'OG0008058', 'OG0008059', 'OG0008060', 'OG0008062', 'OG0008063', 'OG0008065', 'OG0008066', 'OG0008067', 'OG0008068', 'OG0008069', 'OG0008290', 'OG0008291', 'OG0008292', 'OG0008293', 'OG0008294', 'OG0008295', 'OG0008296', 'OG0008297', 'OG0008298', 'OG0008299', 'OG0008300', 'OG0008301', 'OG0008302', 'OG0008304', 'OG0008306', 'OG0008307', 'OG0008308', 'OG0008310', 'OG0008312', 'OG0008313', 'OG0008316', 'OG0008317', 'OG0008318', 'OG0008319', 'OG0008320', 'OG0008322', 'OG0008326', 'OG0008330', 'OG0008332', 'OG0008333', 'OG0008334', 'OG0008335', 'OG0008336', 'OG0008340', 'OG0008342', 'OG0008346']

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
	# print(combd)
	print(fname)
	# print(row)

	for key, value in combd.items():
		if os.path.isdir('{}'.format(fname)) == True:
			pass
		else:
			os.mkdir('{}'.format(fname))
		if isinstance(value, str) == False:
			pass
		else:
			with open('{}/{}.txt'.format(fname, key), 'w') as out:
				out.write('{}\n'.format(value.replace(' ', '').replace(',', '\n')))
