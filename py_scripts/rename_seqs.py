# !/usr/bin/env python3
import os
# import pandas as pd
from Bio import SeqIO

os.chdir('/mnt/mokosz/home/kika/workdir/')
hits = [x for x in os.listdir() if x.endswith('.fa')]
db = open('/mnt/mokosz/home/kika/metamonads/MRO_proteins/metamonads_assemblies/all.seq_dict.tsv')

db_dict = {}
for line in db:
	if line.startswith('original'):
		pass
	else:
		db_dict[line.strip().split('\t')[1]] = line.split('\t')[0]

for file in hits:
	print(file)
	with open('{}.upd.fa'.format(file.split('.fa')[0]), 'w') as out:
		for seq in SeqIO.parse(file, 'fasta'):
			out.write('>{}\n{}\n'.format(db_dict[seq.name], seq.seq))

# table = pd.read_excel('database.xlsx', sheet_name='eukaryotes')
# proteins = [x for x in os.listdir() if x.endswith('muris.faa')]

# prot_dict = {}
# for index, row in table.iterrows():
# 	if row[4] == '-':
# 		pass
# 	else:
# 		if row[0] == 'Metamonada':
# 			prot_dict[row[4]] = row[6]
# 		else:
# 			pass
# # print(prot_dict)

# with open('errors.txt', 'w') as errors, open('Giardia_muris.seq_dict.tsv', 'w') as seqdict:
# 	seqdict.write('original ID\treplaced ID\n')
# 	for file in proteins:
# 			c = 0
# 			print(file)
# 			if file in prot_dict.keys():
# 				with open('{}_renamed.faa'.format(file.split('.')[0]), 'w') as out:
# 					for seq in SeqIO.parse(file, 'fasta'):
# 						c += 1
# 						out.write('>{}_{}\n{}\n'.format(prot_dict[file], c, seq.seq.replace('*', '')))
# 						seqdict.write('{}\t{}_{}\n'.format(seq.description, prot_dict[file], c))
# 			else:
# 				errors.write('{}: Not found\n'.format(file))
