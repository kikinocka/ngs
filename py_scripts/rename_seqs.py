#!/usr/bin/env python3
import os
import pandas as pd
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/metamonada/MRO_proteins/trees/fasta/from_zoli/')
# table = pd.read_excel('database.xlsx', sheet_name='eukaryotes')
proteins = [x for x in os.listdir() if x.endswith('.fasta')]

orgns = {'excADUpa' : 'E-me-Fo-Apal', 'excBLATn' : 'E-me-Pr-Bnau', 'excCARPm' : 'E-me-Fo-Cmem', 'excCHIca' : 'E-me-Fo-Ccau', 
	'excCHIcu' : 'E-me-Fo-Ccus', 'excDYSNb' : 'E-me-Fo-Dbre', 'excERGcy' : 'E-me-Fo-Ecyp', 'Giardia' : 'E-me-Fo-Gint', 
	'excHISTm' : 'E-me-Pa-Hmel', 'excIOTAs' : 'E-me-Fo-Ispi', 'excKIPFb' : 'E-me-Fo-Kbia', 'excMONOe' : 'E-me-Pr-Mexi', 
	'excPTRIp' : 'E-me-Pr-Ppyr', 'excSPIRs' : 'E-me-Fo-Ssal', 'Streblo' : 'E-me-Pr-Sstr', 'excTREPs' : 'E-me-Fo-TPC1', 
	'TVAG' : 'E-me-Pa-Tvag', 'excTRIMm' : 'E-me-Pr-Tmar', 'extTTRIf' : 'E-me-Pa-Tfoe', 'R.caviae' : 'E-me-Fo-Rcav', 
	'R.dobelli' : 'E-me-Fo-Rdob'}


# prot_dict = {}
# for index, row in table.iterrows():
# 	if row[4] == '-':
# 		pass
# 	else:
# 		prot_dict[row[4]] = row[6]

c = 0
# with open('errors.txt', 'w') as errors, open('OGs.seq_dict.tsv', 'w') as seqdict:
for file in proteins:
	print(file)
	# seqdict.write('original ID\treplaced ID\n')
	with open('{}_renamed.fa'.format(file.split('.')[0]), 'w') as out:
		for key in orgns.keys():
			for seq in SeqIO.parse(file, 'fasta'):
				if key in seq.description:
					c += 1
					# print(key)
					# print(seq.description)
					new_acc = '_ '.join(seq.name.split('_')[1:])
					out.write('>{}_{}\n{}\n'.format(orgns[key], new_acc, seq.seq.replace('*','')))
					# seqdict.write('{}\t{}_{}\n'.format(seq.description, orgns[key], c))




		# if file in prot_dict.keys():
# 			with open('renamed/{}'.format(file), 'w') as out:
# 				for seq in SeqIO.parse(file, 'fasta'):
# 					c += 1
# 					out.write('>{}_{}\n{}\n'.format(prot_dict[file], c, seq.seq))
# 					seqdict.write('{}\t{}_{}\n'.format(seq.description, prot_dict[file], c))
# 		else:
# 			errors.write('{}: Not found\n'.format(file))
