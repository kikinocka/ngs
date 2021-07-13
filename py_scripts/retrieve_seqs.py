#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/storage/brno3-cerit/home/kika/oil_sands/Lane26_18S_V9/')
files = [x for x in os.listdir() if x.endswith('.acc')]
database = '/storage/brno3-cerit/home/kika/oil_sands/Lane26_18S_V9/global_dereplicated_1f_representatives.fas'

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
