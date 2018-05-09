#!/usr/bin/env python3
import os
from Bio import SeqIO
from collections import defaultdict


os.chdir('/media/4TB1/blastocrithidia/orthofinder/sg_ogs/alignments/jac_renamed/')
insertions = SeqIO.parse('tryp_ins.txt', 'fasta')
len_results = open('tryp_ins_len.txt', 'w')

len_dict = {}
for ins in insertions:
	print(ins.description)
	if ins.description.split('__')[1].split(' ')[0] in len_dict.keys():
		len_dict[ins.description.split('__')[1].split(' ')[0]] += int(ins.description.split(' ')[1].split('_')[1])
	else:
		len_dict[ins.description.split('__')[1].split(' ')[0]] = int(ins.description.split(' ')[1].split('_')[1])

for key, value in len_dict.items():
	len_results.write('{}\t{}\n'.format(key, value))

len_results.close()