#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/oilsands/metagenomes/ncbi_submission/')
files = [x for x in os.listdir() if x.endswith('.acc')]
database = '/Users/kika/ownCloud/oilsands/metagenomes/ncbi_submission/P3S_NCBI.l200.fa'

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
			if seq.name.split(';')[0] in retrieve:
				# print(seq.name)
				# out.write('>{}\n{}\n'.format(seq.description, seq.seq))
				pass
			else:
				# print(seq.name)
				# pass
				out.write('>{}\n{}\n'.format(seq.description, seq.seq))

