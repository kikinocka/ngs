#!/usr/bin/env python3
import os
from collections import OrderedDict

os.chdir('/home/kika/MEGAsync/diplonema_mt/comparison/')
table = open('1604_multi_modules.tsv')
# out = open('1601st.tsv', 'w')

contigs = OrderedDict(list())
for line in table:
	name = line.split('\t')[0]
	module = line.split('\t')[1]
	mmin = line.split('\t')[2]
	mmax = line.split('\t')[3]
	strand = line.split('\t')[5][:-1]
	if name not in contigs:
		contigs[name] = [(module, mmin, mmax, strand)]
	else:
		contigs[name].append((module, mmin, mmax, strand))

for key, value in contigs.items():
	if len(value) > 1:
		for i in range(len(value)):
			while i < len(value) and i+1 != len(value):
				if value[i][2] > value[i+1][1]:
					if value[i][2] > value[i+1][2]:
						# print(key, value[i], value[i+1])
						# print('embedded')
						if value[i][3] == value[i+1][3]:
							print('{}\t{} [{}]\tsame\n'.format(key, value[i][0], value[i+1][0]))
						else:
							print('{}\t{} [{}]\topposite\n'.format(key, value[i][0], value[i+1][0]))
					else:
						# print(key, value[i], value[i+1])
						# print('overlapping')
						length = int(value[i][2]) - int(value[i+1][1]) + 1
						if value[i][3] == value[i+1][3]:
							print('{}\t{} + {} ({})\tsame\n'.format(key, value[i][0], value[i+1][0], length))
						else:
							print('{}\t{} + {} ({})\topposite\n'.format(key, value[i][0], value[i+1][0], length))

				i += 1
# out.close()