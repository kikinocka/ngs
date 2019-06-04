#!/usr/bin/env python3
import os
import re
from collections import OrderedDict

os.chdir('/home/kika/Dropbox/orthoMCL_kika/orthofasta_full_name/')
files = [x for x in os.listdir() if x.endswith('.fasta')]

with open('euglenids_ko.tsv', 'w') as result, open('errors.txt', 'w') as errors, open('ko_functtion.tsv', 'w') as functions:
	for file in files:
		print(file)
		name = file.split('.')[0]
		euglenids = ['DEEG', 'DEEL', 'DEEE', 'DErc']
		ko_funct = OrderedDict([('DEEG', set()), ('DEEL', set()), ('DEEE', set()), ('DErc', set())])
		funct_dict = {}

		for line in open(file):
			for item in euglenids:
				if item in line:
					try:
						function = line.split('{')[2].split(':')[1][:-2]
						if ',' not in line.split('_')[1].split(':')[1][:-1]:
							ko = line.split('_')[1].split(':')[1][:-1]
							if ko not in funct_dict.keys():
								funct_dict[ko] = function
							else:
								pass
						else:
							ko = line.split('_')[1].split(':')[1][:-1].split(',')
							for i in ko:
								ko_funct[item].update([i])
								if i not in funct_dict.keys():
									funct_dict[i] = function
								else:
									pass
					except IndexError:
						errors.write('{}\n'.format(file))	

		new_ko = {k:v for k,v in ko_funct.items() if len(v) != 0}
		for key, value in new_ko.items():
			result.write('{}'.format(name))
			result.write('\t{}'.format(key))
			for i in sorted(value):
				result.write('\t{}'.format(i))
			result.write('\n')

		for key, value in funct_dict.items():
			functions.write('{}\t{}\n'.format(key, value))
