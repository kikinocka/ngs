#!/usr/bin/env python3
import os
from Bio import SeqIO
from collections import OrderedDict

os.chdir('/home/kika/ownCloud/euglenophytes/OGs/')
files = [x for x in os.listdir() if x.endswith('.txt')]


with open('euglenids_occurence.tsv', 'w') as result, open('euglenids_seq_names.tsv', 'w') as eugl_seqs:
	result.write('\tDEEG\tDEEL\tDEEH\tDEEE\tDERV\tDErc\tDEpt\tDEnp\tDEpv\n')

	for file in files:
		occurence = OrderedDict()
		# # #search in fasta sequences
		# euglenids = OrderedDict([('DEEG', 0), ('DEEZ', 0), ('DEEH', 0), ('DEEE', 0), ('DERV', 0), ('DErc', 0), 
		# 	('DEpt', 0), ('DEnp', 0), ('DEpv', 0)])
		# print(file)
		# name = file.split('.')[0]

		# for seq in SeqIO.parse(file, 'fasta'):
		# 	for key in euglenids.keys():
		# 		if key in seq.description:
		# 			euglenids[key] += 1
		# 			occurence[key] = euglenids[key]
		# 		else:
		# 			occurence[key] = euglenids[key]

		#search in list of names in each group
		for line in open(file):
			euglenids = OrderedDict([('DEEG', 0), ('DEEZ', 0), ('DEEH', 0), ('DEEE', 0), ('DERV', 0), ('DErc', 0), 
				('DEpt', 0), ('DEnp', 0), ('DEpv', 0)])
			f = line.split(':')[0]
			print(f)
			eugl_seqs.write('{}\t'.format(f))
			for i in line.split(':')[1].split(' '):
				for key in euglenids.keys():
					if key in i:
						print(i)
						eugl_seqs.write('{},'.format(i))
						euglenids[key] += 1
						occurence[key] = euglenids[key]
					else:
						occurence[key] = euglenids[key]
			eugl_seqs.write('\n')
		
			result.write('{}'.format(f))
			for key, value in occurence.items():
				result.write('\t{}'.format(value))
			result.write('\n')
