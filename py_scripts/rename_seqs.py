#!/usr/bin/env python3
import os
import pandas as pd
from Bio import SeqIO

os.chdir('/mnt/mokosz/home/kika/allDB/archaea/')
table = pd.read_excel('database.xlsx', sheet_name='archaea')
proteins = [x for x in os.listdir() if x.endswith('.fa')]


prot_dict = {}
for index, row in table.iterrows():
	if row[4] == '-':
		pass
	else:
		prot_dict[row[4]] = row[5]

for file in proteins:
	print(file)
	with open('errors.txt', 'w') as errors, open('aenigm.seq_dict.tsv', 'w') as seqdict:
		c = 0
		seqdict.write('original ID\treplaced ID\n')
		if file in prot_dict.keys():
			with open('{}'.format(file), 'w') as out:
				for seq in SeqIO.parse(file, 'fasta'):
					c += 1
					out.write('>{}_{}\n{}\n'.format(prot_dict[file], c, seq.seq))
					seqdict.write('{}\t{}_{}\n'.format(seq.description, prot_dict[file], c))
		else:
			errors.write('{}: Not found\n'.format(file))
