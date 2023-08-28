#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/mnt/mokosz/home/kika/metamonads_ancestral/hmm_hits/')
files = [x for x in os.listdir() if x.endswith('hmm_hits.fa')]

for file in files:
	eval_dict = {}
	print(file)
	for seq in SeqIO.parse(file, 'fasta'):
		orgn = seq.name.split('_')[0]
		eval = float(seq.description.split(' ')[1].split(':')[1])
		
		if orgn not in eval_dict:
			eval_dict[orgn]	= [[eval, seq.description, str(seq.seq).replace('*', '')]]
		else:
			eval_dict[orgn].append([eval, seq.description, str(seq.seq).replace('*', '')])

	with open('{}.reduced.fa'.format(file.split('.fa')[0]), 'w') as out:
		for key, value in eval_dict.items():
			if len(value) > 3:
				value = value[0:3]
			for v in value:
				out.write('>{}\n{}\n'.format(v[1], v[2]))
