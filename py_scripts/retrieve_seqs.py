#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/Mic60-Mgm1-Opa1/coevolution/opa1/')
files = [x for x in os.listdir() if x.endswith('.acc')]
database = '/Users/kika/ownCloud/Mic60-Mgm1-Opa1/dynamins_tree/ver1/dynamins.fa'

for accessions in files: 
	print(accessions)
	fname = accessions.split('.acc')[0]
	retrieve = set()

	with open('{}.fa'.format(fname), 'w') as out:
		db = SeqIO.parse(database, 'fasta')

		for line in open(accessions):
			retrieve.add(line[:-1])

		for seq in db:
			if seq.name in retrieve:
				out.write('>{}\n{}\n'.format(seq.description, seq.seq))
			else:
				# print(seq.description)
				pass
