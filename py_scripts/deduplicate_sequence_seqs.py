#!/usr/bin/env python3
import os
from Bio import SeqIO
from collections import defaultdict, OrderedDict

os.chdir('/Users/kika/ownCloud/kinetoplastids/angomonas/EAPs/')
infile = SeqIO.parse('three.fa', 'fasta')
out_fasta = open('three_deduplicated.fa', 'w')
out_names = open('three_dupl-names.txt', 'w')

multiplications = defaultdict(list)
seq_dict = OrderedDict()
for seq in infile:
	sequence = seq.seq.upper()
	multiplications[sequence].append(seq.description)
	if sequence not in seq_dict:
		# # #rename full header only with name (acc, till the first space)
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
