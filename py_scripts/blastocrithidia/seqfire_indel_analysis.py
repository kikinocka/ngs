#!/usr/bin/env python3
import os
from collections import defaultdict

os.chdir('/home/kika/ownCloud/blastocrithidia/seqfire/')
files = sorted(os.listdir())
tbruc_out = open('indel_analysis_tbruc.tsv', 'w')
jac_out = open('indel_analysis_jac.tsv', 'w')
p57_out = open('indel_analysis_p57.tsv', 'w')
triat_out = open('indel_analysis_triat.tsv', 'w')
bexlh_out = open('indel_analysis_bexlh.tsv', 'w')

def find_ins(file, species):
	species_ins = defaultdict(list)
	if file.endswith('.indel'):
		file_name = file.split('.')[0]
		print(file_name)
		for line in open(file):
			if line.startswith(species):
				gene = '{}_{}'.format(file_name, line.split(' ')[0].split('_')[1])
				ins = line.split(' ')[5].replace('-', '').replace('?', '')
				species_ins[gene].append(ins)
	else:
		pass
	return species_ins


for file in files:
	tbruc = find_ins(file, 'Tbrutreu')
	for key, value in tbruc.items():
		for i, x in enumerate(value):
			index = i + 1
			tbruc_out.write('{}\tins{}\t{}\t{}\n'.format(key, index, x, len(x)))

	jac = find_ins(file, 'Jac')
	for key, value in jac.items():
		for i, x in enumerate(value):
			index = i + 1
			jac_out.write('{}\tins{}\t{}\t{}\n'.format(key, index, x, len(x)))

	p57 = find_ins(file, 'Bp57')
	for key, value in p57.items():
		for i, x in enumerate(value):
			index = i + 1
			p57_out.write('{}\tins{}\t{}\t{}\n'.format(key, index, x, len(x)))

	triat = find_ins(file, 'Btri')
	for key, value in triat.items():
		for i, x in enumerate(value):
			index = i + 1
			triat_out.write('{}\tins{}\t{}\t{}\n'.format(key, index, x, len(x)))

	bexlh = find_ins(file, 'Bexl')
	for key, value in bexlh.items():
		for i, x in enumerate(value):
			index = i + 1
			bexlh_out.write('{}\tins{}\t{}\t{}\n'.format(key, index, x, len(x)))

tbruc_out.close()
jac_out.close()
p57_out.close()
triat_out.close()
bexlh_out.close()

# def write_file(new_file, species_ins):
# 	out = open(new_file, 'w')
# 	for key, value in species_ins.items():
# 		for i, x in enumerate(value):
# 			if x == '':
# 				pass
# 			else:
# 				index = i + 1
# 				print(key, index, x, len(x))
# 				out.write('{}\tins{}\t{}\t{}\n'.format(key, index, x, len(x)))
# 	# out.close()

# write_file('indel_analysis_tbruc.tsv', tbruc)
# write_file('indel_analysis_jac.tsv', jac)
# write_file('indel_analysis_p57.tsv', p57)
# write_file('indel_analysis_triat.tsv', triat)
# write_file('indel_analysis_bexlh.tsv', bexlh)
