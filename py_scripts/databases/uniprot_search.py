#!/usr/bin/env python3
import os
from bioservices import UniProt as UP

os.chdir('/Users/kika/ownCloud/membrane-trafficking/clathrin/joel_roca/')
acc_files = [x for x in os.listdir() if x.endswith('.acc')]

# for acc_file in acc_files:
# 	print(acc_file)
# 	name = acc_file.split('_')[0]
# 	with open('{}_uniprot.fa'.format(name), 'w') as result:
# 		for acc in open(acc_file):
# 			print(acc.strip())
# 			seq = UP().retrieve(acc.strip(), frmt='fasta')
# 			result.write('{}'.format(seq))


for acc_file in acc_files:
	print(acc_file)
	name = acc_file.split('.')[0]
	with open('{}_uniprot.tsv'.format(name), 'w') as result, open('{}_uniprot.errors.txt'.format(name), 'w') as errors:
		for acc in open(acc_file):
			print(acc.strip())
			try:
				taxonomy = list(UP().retrieve(acc.strip()).values())[5]['lineage']
				taxonomy = str(taxonomy).replace('[', '').replace(']', '').replace('\'', '')
				result.write('{}\t{}\n'.format(acc.strip(), taxonomy))
			except:
				errors.write('{}\n'.format(acc.strip())
