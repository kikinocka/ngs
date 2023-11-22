#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/mnt/mokosz/home/kika/metamonads_ancestral/metamonads_assemblies/')
files = [x for x in os.listdir() if x.endswith('gmur.acc')]
database = '/mnt/mokosz/home/kika/allDB/eukaryotes/Giardia_muris.faa'

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
			if seq.name.split('-')[0] in retrieve:
				# print(seq.name)
				out.write('>{}\n{}\n'.format(seq.description, seq.seq))
				# pass
			else:
				pass
				# out.write('>{}\n{}\n'.format(seq.description, seq.seq))

