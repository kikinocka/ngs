#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/membrane-trafficking/TSET_haptophytes/stramenopiles-haptophytes/ver2/prop-sol/')
files = [x for x in os.listdir() if x.endswith('in.acc')]
database = 'prop-sol.fa'

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
			# print(seq.name)
			# name = seq.description.split(' ')[4]
			if seq.name in retrieve:
				# print(seq.name)
				out.write('>{}\n{}\n'.format(seq.description, seq.seq))
				# pass
			else:
				# print(seq.name)
				# out.write('>{}\n{}\n'.format(seq.description, seq.seq))
				pass

