#!/usr/bin/env python3
import os
from collections import defaultdict

os.chdir('/home/kika/ownCloud/blastocrithidia/seqfire/')
files = sorted(os.listdir())

def find_ins(file):
	tbruc_ins = defaultdict(list)
	jac_ins = defaultdict(list)
	if file.endswith('.indel'):
		file_name = file.split('.')[0]
		print(file_name)
		for line in open(file):
			if line.startswith('Tbrutreu'):
				gene = '{}_{}'.format(file_name, line.split(' ')[0].split('_')[1])
				ins = line.split(' ')[5].replace('-', '').replace('?', '')
				tbruc_ins[gene].append(ins)
			elif line.startswith('Jac'):
				gene = '{}_{}'.format(file_name, line.split(' ')[0].split('_')[1])
				ins = line.split(' ')[5].replace('-', '').replace('?', '')
				jac_ins[gene].append(ins)
	else:
		pass
	return tbruc_ins, jac_ins

with open('indel_analysis_tbruc.tsv', 'w') as tbruc_out:
	for file in files:
		tbruc = find_ins(file)[0]
		for key, value in tbruc.items():
			for i, x in enumerate(value):
				if x == '':
					pass
				else:
					index = i +1
					tbruc_out.write('{}\tins{}\t{}\t{}\n'.format(key, index, x, len(x)))

with open('indel_analysis_jac.tsv', 'w') as jac_out:
	for file in files:
		jac = find_ins(file)[1]
		for key, value in jac.items():
			for i, x in enumerate(value):
				if x == '':
					pass
				else:
					index = i +1
					jac_out.write('{}\tins{}\t{}\t{}\n'.format(key, index, x, len(x)))
