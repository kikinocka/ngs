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

out.close()