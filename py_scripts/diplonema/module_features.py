#!/usr/bin/env python3
import os
from collections import OrderedDict

os.chdir('/home/kika/MEGAsync/diplonema_mt/comparison/')
table = open('1604_multi_modules.tsv')
out = open('1601st.txt', 'w')

class Contig:
	def __init__(self, name):
		self.name = name
		self.mod_coordinates = []

	def add_module(self, module, mmin, mmax, strand):
		self.mod_coordinates.append((module, mmin, mmax, strand))

		
all_contigs = []
for line in table:
	contig = Contig(line.split('\t')[0])
	module = line.split('\t')[1]
	mmin = line.split('\t')[2]
	mmax = line.split('\t')[3]
	strand = line.split('\t')[5][:-1]
	contig.add_module(module, mmin, mmax, strand)
	all_contigs.append(contig)

print(all_contigs)

# for contig in all_contigs:
# 	print(contig.name, contig.mod_coordinates)

# contigs = OrderedDict(list())
# for line in table:
# 	name = line.split('\t')[0]
# 	module = line.split('\t')[1]
# 	mmin = line.split('\t')[2]
# 	mmax = line.split('\t')[3]
# 	strand = line.split('\t')[5][:-1]
# 	if name not in contigs:
# 		contigs[name] = [(module, mmin, mmax, strand)]
# 	else:
# 		contigs[name].append((module, mmin, mmax, strand))

# for key, value in contigs.items():
# 	# if len(value) == 2:
# 	# 	print(key, value)
# 	# 	print('2')
# 	# 	# if value[0][2] > value[1][1]:
# 	# 	# 	if value[0][2] > value[1][2]:
# 	# 	# 		if value[0][3] == value[1][3]:
# 	# 	# 			out.write('{}\t{} [{}]\tsame\n'.format(key, value[0][0], value[1][0]))
# 	# 	# 		else:
# 	# 	# 			out.write('{}\t{} [{}]\topposite\n'.format(key, value[0][0], value[1][0]))
# 	# 	# 	else:
# 	# 	# 		length = int(value[0][2]) - int(value[1][1]) + 1
# 	# 	# 		if value[0][3] == value[1][3]:
# 	# 	# 			out.write('{}\t{} + {} ({})\tsame\n'.format(key, value[0][0], value[1][0], length))
# 	# 	# 		else:
# 	# 	# 			out.write('{}\t{} + {} ({})\topposite\n'.format(key, value[0][0], value[1][0], length))
# 	# else:
# 	for i in range(len(value)):
# 		# print(key, value, i)
# 		while i < len(value):
# 			print(key, value)
# 			if i+1 == len(value):
# 				pass
# 			i += 1

out.close()