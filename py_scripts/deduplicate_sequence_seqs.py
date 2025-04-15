#!/usr/bin/env python3
import os
from Bio import SeqIO
from collections import defaultdict, OrderedDict

os.chdir('/Users/kika/ownCloud/metamonada/MRO_proteins/fasttree/last6/')
files = [x for x in os.listdir() if x.endswith('Tv113880+Tv442170.mro+hmm.final.fa')]

for infile in files:
	print(infile)
	out_fasta = open('{}_deduplicated.fa'.format(infile.split('.fa')[0]), 'w')
	out_names = open('{}_dupl-names.txt'.format(infile.split('.fa')[0]), 'w')
	multiplications = defaultdict(list)
	seq_dict = OrderedDict()

	for seq in SeqIO.parse(infile, 'fasta'):
		sequence = seq.seq.upper()
		multiplications[sequence].append(seq.description)
		if sequence not in seq_dict:
			# #rename full header only with name
			# seq_dict[sequence] = seq.name 
			#keep full header			
			seq_dict[sequence] = seq.description

	for key, value in seq_dict.items():
		out_fasta.write('>{}\n{}\n'.format(value, key))

	for key, value in multiplications.items():
		if len(value) > 1:
			out_names.write('{}\n'.format(str(value)))

out_fasta.close()
out_names.close()
