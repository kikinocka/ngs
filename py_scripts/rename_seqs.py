#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/mnt/mokosz/home/kika/allDB/eukaryotes/')
table = pd.read_excel('database.xlsx', sheet_name='eukaryotes')
proteins = [x for x in os.listdir() if x.endswith('.faa')]


prot_dict = {}
for index, row in table.iterrows():
	fname = row[4]
	pname = row[6]
	print(fname)
	prot_dict[fname] = pname

for file in proteins:
	if file in prot_dict.keys():
		with open('renamed/{}'.format(file), 'w') as out:
			for seq in SeqIO.parse(file, 'fasta'):
				out.write('>{}\n{}\n'.format(prot_dict[file], seq.seq))
	else:
		print('{}: Not found\n'.format(file))
