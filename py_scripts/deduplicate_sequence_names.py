#!/usr/bin/env python3
import os
from Bio import SeqIO
from collections import OrderedDict
from collections import defaultdict

os.chdir('/mnt/mokosz/home/kika/metamonads/MRO_proteins/2-hmm_hits/')
files = [x for x in os.listdir() if x.endswith('reduced.fa')]

for infile in files:
	print(infile)
	with open('{}_deduplicated.fa'.format(infile.split('.fa')[0]), 'w') as out_fasta, \
		 open('{}_dupl-names.txt'.format(infile.split('.fa')[0]), 'w') as out_names:
		multiplications = defaultdict(list)
		seq_dict = OrderedDict()
		for sequence in SeqIO.parse(infile, 'fasta'):
			multiplications[sequence.name].append(sequence.description)
			if sequence.name not in seq_dict:
				seq_dict[sequence.name] = [sequence.description, sequence.seq]

		for key, value in seq_dict.items():
			out_fasta.write('>{}\n{}\n'.format(value[0], value[1]))

		for key, value in multiplications.items():
			if len(value) > 1:
				out_names.write('{}\n'.format(str(value)))
