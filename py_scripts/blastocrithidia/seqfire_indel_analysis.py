#!/usr/bin/env python3
import os
import re
from Bio import AlignIO
from collections import defaultdict

os.chdir('/home/kika/ownCloud/blastocrithidia/seqfire/complex_ins/')
files = sorted(os.listdir())
# aln_out = open('aln_len.tsv', 'w')

def find_species(file):
	species = set()
	for line in open(file):
		if '_' in line:
			sp = line.split(' ')[0].split('_')[0]
			species.add(sp)
	return species

def find_ins(file, species):
	ins_dict = defaultdict(list)
	file_name = file.split('_')[0]
	for line in open(file):
		if line.startswith(species):
			ins = re.sub(r'.*: \w  (.*)  \w', r'\g<1>', line)
			ins = ins.replace('-', '').replace('  **', '')[:-1]
			ins_dict[file_name].append(ins)
	return ins_dict


# for file in files:
# 	if file.endswith('.aln'):
# 		f_name = file.split('.')[0]
# 		aln = AlignIO.read(file, 'fasta')
# 		length = aln.get_alignment_length()
# 		aln_out.write('{}\t{}\n'.format(f_name, length))

for file in files:
	if file.endswith('.indel'):
		print(file)
		species = find_species(file)
		for sp in species:
			with open('indel_analysis_{}.tsv'.format(sp), 'a') as out:
				spp = find_ins(file, sp)
				for key, value in spp.items():
					for i, x in enumerate(value):
						index = i + 1
						out.write('{}\tins{}\t{}\t{}\n'.format(key, index, x, len(x)))
			with open('all_indels_{}.tsv'.format(sp), 'a') as out2:
				full_len = 0
				non_zero = 0
				spp = find_ins(file, sp)
				for key, value in spp.items():
					for i, x in enumerate(value):
						index = i + 1
						full_len += len(x)
						if len(x) != 0:
							non_zero += 1
				out2.write('{}\t{}\t{}\t{}\n'.format(key, index, non_zero, full_len))
