#!/usr/bin/env python3
import os
import pandas as pd
from Bio import SeqIO

os.chdir('/mnt/mokosz/home/kika/metamonads_ancestral/OGs_fasta/')
# table = pd.read_excel('database.xlsx', sheet_name='eukaryotes')
proteins = [x for x in os.listdir() if x.endswith('.fa')]

orgns = {'Carplike' : 'E-me-Fo-Apal', 'BLNAU' : 'E-me-Pr-Bnau', 'Carpediemonas' : 'E-me-Fo-Cmem', 'caulleri' : 'E-me-Fo-Ccau', 
	'cuspidata' : 'E-me-Fo-Ccus', 'Dysnectes' : 'E-me-Fo-Dbre', 'Ergobibamus' : 'E-me-Fo-Ecyp', 'Giardia' : 'E-me-Fo-Gint', 
	'Histomonas' : 'E-me-Pa-Hmel', 'Iotanema' : 'E-me-Fo-Ispi', 'Kipferlia' : 'E-me-Fo-Kbia', 'MONOS' : 'E-me-Pr-Mexi', 
	'PAPYR' : 'E-me-Pr-Ppyr', 'Spironucleus' : 'E-me-Fo-Ssal', 'Streblo' : 'E-me-Pr-Sstr', 'Trepomonas_PC1' : 'E-me-Fo-TPC1', 
	'TVAG' : 'E-me-Pa-Tvag', 'Trimastix' : 'E-me-Pr-Tmar', 'Tritrichomonas' : 'E-me-Pa-Tfoe'}


# prot_dict = {}
# for index, row in table.iterrows():
# 	if row[4] == '-':
# 		pass
# 	else:
# 		prot_dict[row[4]] = row[6]

c = 0
for file in proteins:
	print(file)
	with open('errors.txt', 'w') as errors, open('OGs.seq_dict.tsv', 'w') as seqdict:
		seqdict.write('original ID\treplaced ID\n')
		with open('{}_renamed.fa'.format(file.split('.')[0]), 'w') as out:
			for key in orgns.keys():
				for seq in SeqIO.parse(file, 'fasta'):
					if key in seq.description:
						c += 1
						# print(key)
						# print(seq.description)
						out.write('>{}_{}\n{}\n'.format(orgns[key], c, seq.seq))
						seqdict.write('{}\t{}_{}\n'.format(seq.description, orgns[key], c))




		# if file in prot_dict.keys():
# 			with open('renamed/{}'.format(file), 'w') as out:
# 				for seq in SeqIO.parse(file, 'fasta'):
# 					c += 1
# 					out.write('>{}_{}\n{}\n'.format(prot_dict[file], c, seq.seq))
# 					seqdict.write('{}\t{}_{}\n'.format(seq.description, prot_dict[file], c))
# 		else:
# 			errors.write('{}: Not found\n'.format(file))
