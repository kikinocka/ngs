#!/usr/bin/env python3
import os
from Bio import SeqIO
from collections import OrderedDict
from collections import defaultdict

os.chdir('/mnt/mokosz/home/kika/metamonads/MRO_proteins/3-MRO+HMMhits_fasta/')
files = [x for x in os.listdir() if x.endswith('.fa')]
# infile = SeqIO.parse('CAD2216821.fa', 'fasta')
# out_fasta = open('CAD2216821_deduplicated.fa', 'w')
# out_names = open('CAD2216821_dupl-names.txt', 'w')

# names = []
# with open('RABs_deduplicated.fa', 'w') as out:
# 	for seq in infile:
# 		if seq.name.lower() not in names:
# 			names.append(seq.name.lower())
# 			new_name = seq.name.replace('|', '_')
# 			new_desc = '{} {}'.format(new_name, ' '.join(seq.description.split()[1:]))
# 			out.write('>{}\n{}\n'.format(new_desc[:50], seq.seq))
# 			print(seq.name + ' not in names')
# 		else:
# 			names.append(seq.name.lower())
# 			new_name = '{}_{}'.format(seq.name.replace('|', '_'), names.count(seq.name.lower()))
# 			new_desc = '{} {}'.format(new_name, ' '.join(seq.description.split()[1:]))
# 			out.write('>{}\n{}\n'.format(new_desc[:50], seq.seq))
# 			print('{} changed to {}'.format(seq.name, new_name))

for infile in files:
	print(infile)
	with open('{}_deduplicated.fa'.format(infile.split('.fa')[0]), 'w') as out_fasta, \
		 open('{}_dupl-names.txt'.format(infile.split('.fa')[0]), 'w') as out_names:
		multiplications = defaultdict(list)
		seq_dict = OrderedDict()
		for sequence in SeqIO.parse(infile):
			multiplications[sequence.name].append(sequence.description)
			if sequence.name not in seq_dict:
				seq_dict[sequence.name] = [sequence.description, sequence.seq]

		for key, value in seq_dict.items():
			out_fasta.write('>{}\n{}\n'.format(value[0], value[1]))

		for key, value in multiplications.items():
			if len(value) > 1:
				out_names.write('{}\n'.format(str(value)))

# out_fasta.close()
# out_names.close()
