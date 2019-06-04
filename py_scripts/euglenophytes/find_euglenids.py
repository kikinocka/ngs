#!/usr/bin/env python3
import os
from Bio import SeqIO
from collections import OrderedDict

os.chdir('/home/kika/Dropbox/orthoMCL_kika/orthofasta/')
files = [x for x in os.listdir() if x.endswith('.fas')]


with open('euglenids_occurence.tsv', 'w') as result:
	result.write('\tDEEG\tDEEL\tDEEH\tDEEE\tDERV\tDErc\tDEpt\tDEnp\tDEpv\n')

	for file in files:
		print(file)
		name = file.split('.')[0]
		euglenids = OrderedDict([('DEEG', 0), ('DEEL', 0), ('DEEH', 0), ('DEEE', 0), ('DERV', 0), ('DErc', 0), 
		('DEpt', 0), ('DEnp', 0), ('DEpv', 0)])
		occurence = OrderedDict()

		for seq in SeqIO.parse(file, 'fasta'):
			for key in euglenids.keys():
				if key in seq.description:
					euglenids[key] += 1
					occurence[key] = euglenids[key]
				else:
					occurence[key] = euglenids[key]
		
		result.write('{}'.format(name))
		for key, value in occurence.items():
			result.write('\t{}'.format(value))
		result.write('\n')
