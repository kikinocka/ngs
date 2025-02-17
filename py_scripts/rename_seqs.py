#!/usr/bin/env python3
import os
import pandas as pd
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/metamonada/assemblies/renamed/')
table = pd.read_excel('database.xlsx', sheet_name='eukaryotes')
proteins = [x for x in os.listdir() if x.endswith('.faa')]

prot_dict = {}
for index, row in table.iterrows():
	if row[4] == '-':
		pass
	else:
		if row[0] == 'Metamonada':
			prot_dict[row[4]] = row[6]
		else:
			pass
# print(prot_dict)

with open('errors.txt', 'w') as errors, open('metamonads_in_OGs.seq_dict.tsv', 'w') as seqdict:
	seqdict.write('original ID\treplaced ID\n')
	for file in proteins:
			c = 0
			print(file)
			if file in prot_dict.keys():
				with open('{}_renamed.faa'.format(file.split('.')[0]), 'w') as out:
					for seq in SeqIO.parse(file, 'fasta'):
						c += 1
						out.write('>{}_{}\n{}\n'.format(prot_dict[file], c, seq.seq.replace('*', '')))
						seqdict.write('{}\t{}_{}\n'.format(seq.description, prot_dict[file], c))
			else:
				errors.write('{}: Not found\n'.format(file))

