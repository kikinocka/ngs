#!/usr/bin/env python3
import os
from collections import OrderedDict

os.chdir('/home/kika/MEGAsync/diplonema_mt/comparison/')
table = open('1604_multi_modules.tsv')
# out = open('1601st.txt', 'w')

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
			# print(key, value, i, len(value))
			while i < len(value):
				print(key, value[i])
				# if value[i][2] > value[i+1][1]:
				# 	print(key, value)

				i += 1
