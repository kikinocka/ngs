#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/storage/brno3-cerit/home/kika/tRNAs-kinetoplastids/')
files = [x for x in os.listdir() if x.endswith('.acc')]
database = '/storage/brno3-cerit/home/kika/tRNAs-kinetoplastids/read_DB/Tbrucei-cyto.fa'

for accessions in files: 
	print(accessions)
	fname = accessions.split('.acc')[0]
	retrieve = set()

	with open('{}.fa'.format(fname), 'w') as out:
		db = SeqIO.parse(database, 'fasta')

		for line in open(accessions):
			retrieve.add(line[:-1])
		# print(retrieve)
		for seq in db:
			if seq.name.split(';')[0] in retrieve:
				out.write('>{}\n{}\n'.format(seq.description, seq.seq))
			else:
				# print(seq.description)
				pass
