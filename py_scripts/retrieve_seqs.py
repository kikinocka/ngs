#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/blasto_comparative/count_software/all_Blastos_expansions/')
files = [x for x in os.listdir() if x.endswith('.acc')]
database = '/Users/kika/ownCloud/blasto_comparative/proteins/FINAL/Btri_proteins-final.faa'

for accessions in files: 
	print(accessions)
	fname = accessions.split('.acc')[0]
	retrieve = set()

	with open('{}.fa'.format(fname), 'w') as out:
		db = SeqIO.parse(database, 'fasta')
		# print(db)
		for line in open(accessions):
			retrieve.add(line[:-1])
		# print(retrieve)
		for seq in db:
			if seq.name in retrieve:
				# print(seq.name)
				out.write('>{}\n{}\n'.format(seq.description, seq.seq))
				# pass
			else:
				# print(seq.name)
				pass
				# out.write('>{}\n{}\n'.format(seq.description, seq.seq))

