#!/usr/bin/env python3
import os
import pandas as pd

os.chdir('/Users/kika/ownCloud/blasto_comparative/proteins/companion/')
gff = open('Omod/scaffold.out.gff3')
excel = pd.read_excel('Omod_annotations.xlsx', header=None, usecols=("A:B"))

acc_dict ={}
for index, row in excel.iterrows():
	acc_dict[row[1].split('.')[0]] = row[0]
# print(acc_dict)

with open('Omod_companion.gff3', 'w') as out:
	for line in gff:
		if line.startswith('#'):
			out.write(line)
		elif line.split('\t')[2] == 'contig':
			out.write(line)
		elif line.split('\t')[2] == 'gap':
			out.write(line)
		else:
			line = line.strip()
			old = str()
			try:	
				if line.split('\t')[2] == 'gene':
					# print('found gene: ', line.split('\t')[8].split('=')[1].split(';')[0])
					old = line.split('\t')[8].split('=')[1].split(';')[0]
				elif line.split('\t')[2] == 'pseudogene':
					# print('found pseudogene')
					old = line.split('\t')[8].split('=')[1].split(':')[0]
				else:
					# print('found else')
					old = line.split('\t')[8].split('=')[1].split(';')[0].split('.')[0]
				out.write(line.replace(old, acc_dict[old]) + '\n')
			except:
				print(line.split('\t')[2], line.split('\t')[8].split('=')[1])
