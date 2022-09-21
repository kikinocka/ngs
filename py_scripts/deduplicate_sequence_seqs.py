#!/usr/bin/env python3
import os
from Bio import SeqIO
from collections import defaultdict, OrderedDict

os.chdir('/Users/kika/ownCloud/membrane-trafficking/angomonas_SNAREs/')
infile = SeqIO.parse('adea_r.fa', 'fasta')
out_fasta = open('adea_r_deduplicated.fa', 'w')
out_names = open('adea_r_dupl-names.txt', 'w')

multiplications = defaultdict(list)
seq_dict = OrderedDict()
for sequence in infile:
	multiplications[sequence.seq].append(sequence.description)
	if sequence.seq not in seq_dict:
		# # #rename full header only with name (acc, till the first space)
		# seq_dict[sequence.seq] = sequence.name 
		#keep full header			
		seq_dict[sequence.seq] = sequence.description

for key, value in seq_dict.items():
	out_fasta.write('>{}\n{}\n'.format(value, key))

for key, value in multiplications.items():
	if len(value) > 1:
		out_names.write('{}\n'.format(str(value)))

out_fasta.close()
out_names.close()
