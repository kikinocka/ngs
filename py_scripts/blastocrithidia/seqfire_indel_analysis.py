#!/usr/bin/env python3
import os
from collections import defaultdict

os.chdir('/home/kika/ownCloud/blastocrithidia/seqfire/')
files = sorted(os.listdir())

def find_ins(file):
	tbruc_ins = defaultdict(list)
	jac_ins = defaultdict(list)
	p57_ins = defaultdict(list)
	triat_ins = defaultdict(list)
	bexlh_ins = defaultdict(list)
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
			elif line.startswith('Bp57'):
				gene = '{}_{}'.format(file_name, line.split(' ')[1])
				ins = line.split(' ')[5].replace('-', '').replace('?', '')
				p57_ins[gene].append(ins)
			elif line.startswith('Btri'):
				gene = '{}_{}'.format(file_name, line.split(' ')[1])
				ins = line.split(' ')[5].replace('-', '').replace('?', '')
				triat_ins[gene].append(ins)
			elif line.startswith('Bexl'):
				gene = '{}_{}'.format(file_name, line.split(' ')[1])
				ins = line.split(' ')[5].replace('-', '').replace('?', '')
				bexlh_ins[gene].append(ins)
	else:
		pass
	return tbruc_ins, jac_ins, p57_ins, triat_ins, bexlh_ins

with open('indel_analysis_tbruc.tsv', 'w') as tbruc_out:
	for file in files:
		tbruc = find_ins(file)[0]
		for key, value in tbruc.items():
			for i, x in enumerate(value):
				if x == '':
					pass
				else:
					index = i + 1
					tbruc_out.write('{}\tins{}\t{}\t{}\n'.format(key, index, x, len(x)))

with open('indel_analysis_jac.tsv', 'w') as jac_out:
	for file in files:
		jac = find_ins(file)[1]
		for key, value in jac.items():
			for i, x in enumerate(value):
				if x == '':
					pass
				else:
					index = i + 1
					jac_out.write('{}\tins{}\t{}\t{}\n'.format(key, index, x, len(x)))

with open('indel_analysis_p57.tsv', 'w') as p57_out:
	for file in files:
		p57 = find_ins(file)[2]
		for key, value in p57.items():
			for i, x in enumerate(value):
				if x == '':
					pass
				else:
					index = i + 1
					p57_out.write('{}\tins{}\t{}\t{}\n'.format(key, index, x, len(x)))

with open('indel_analysis_triat.tsv', 'w') as triat_out:
	for file in files:
		triat = find_ins(file)[3]
		for key, value in triat.items():
			for i, x in enumerate(value):
				if x == '':
					pass
				else:
					index = i + 1
					triat_out.write('{}\tins{}\t{}\t{}\n'.format(key, index, x, len(x)))

with open('indel_analysis_bexlh.tsv', 'w') as bexlh_out:
	for file in files:
		bexlh = find_ins(file)[4]
		for key, value in bexlh.items():
			for i, x in enumerate(value):
				if x == '':
					pass
				else:
					index = i + 1
					bexlh_out.write('{}\tins{}\t{}\t{}\n'.format(key, index, x, len(x)))
