#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Dcko/ownCloud/MMETSP1310/')
files = [x for x in os.listdir() if x.endswith('.acc')]
database = '/Dcko/MEGAsync/Data/MMETSP1310.nt.fa.txt'

for accessions in files: 
	print(accessions)
	fname = accessions.split('.')[0]
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
