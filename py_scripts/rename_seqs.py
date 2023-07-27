#!/usr/bin/env python3
import os
import pandas as pd
from Bio import SeqIO

os.chdir('/mnt/mokosz/home/kika/allDB/eukaryotes/')
table = pd.read_excel('database.xlsx', sheet_name='eukaryotes')
proteins = [x for x in os.listdir() if x.endswith('.faa')]


prot_dict = {}
for index, row in table.iterrows():
	fname = row[4]
	pname = row[6]
	if fname == '-':
		pass
	else:
		prot_dict[fname] = pname

for file in proteins:
	print(file)
	with open('renamed/errors.txt', 'w') as errors:
		c = 0
		seqdict.write('original ID\treplaced ID\n')
		if file in prot_dict.keys():
			with open('renamed/{}'.format(file), 'w') as out:
				for seq in SeqIO.parse(file, 'fasta'):
					c += 1
					out.write('>{}_{} {}\n{}\n'.format(prot_dict[file], c, seq.description, seq.seq))
		else:
			errors.write('{}: Not found\n'.format(file))
