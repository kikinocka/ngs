#!/usr/bin/env python3
import os
import re
from Bio import AlignIO
from collections import defaultdict

os.chdir('/home/kika/ownCloud/blastocrithidia/seqfire/ins_div_by_clade')
files = sorted(os.listdir())

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

jaculum = []
leishmania = []
trypanosoma = []
crithidia = []
leptomonas = []
phytomonas = []
blechomonas = 0
paratrypka = 0

for file in files:
	if file.endswith('_replaced.indel'):
		print(file)
		species = find_species(file)
		for sp in species:
			spp = find_ins(file, sp)
			for key, value in spp.items():
				if sp in ['Bp57', 'Bexl', 'Btri', 'Jac']:
					# print(sp)
					# ins_len = 0
					# for i in value:
					# 	ins_len += len(i)
					# print(ins_len)
					print(sp, value)
				elif sp in ['Ldon', 'LmajSD', 'Lmex', 'LmajLV', 'Ltro', 'Ltur', 'Lspmar', 'Lpan', 'Laet', 'Ladl', 
					'Lenr', 'LmajF', 'Lara', 'Lger', 'Emont']:
					print(sp, value)
				elif sp in ['Tran', 'Tcru1', 'Tbrug', 'Tbrutreu', 'Tmar', 'Tviv', 'Tcon', 'Teva', 'Tcru2']:
					print(sp, value)
				elif sp in ['Cmel', 'Cexp', 'Cbom', 'Cfas']:
					print(sp, value)
				elif sp in ['Lsey', 'LpyrH10']:
					print(sp, value)
				elif sp in ['Phart', 'Pem1']:
					print(sp, value)
				elif sp == 'Bayal':
					print(sp, value)
				elif sp == 'Pcon':
					print(sp, value)
				else:
					print(sp)
