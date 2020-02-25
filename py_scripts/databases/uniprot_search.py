#!/usr/bin/env python3
import os
from bioservices import UniProt as up

os.chdir('/Dcko/ownCloud/proteromonas/SOD_tree/')
acc_files = [x for x in os.listdir() if x.endswith('.acc')]

for acc_file in acc_files:
	print(acc_file)
	name = acc_file.split('_')[0]
	with open('{}_uniprot.fa'.format(name), 'w') as result:
		for acc in open(acc_file):
			print(acc.strip())
			seq = up().retrieve(acc.strip(), 'fasta')
			result.write('{}'.format(seq))
