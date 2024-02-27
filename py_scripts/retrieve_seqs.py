#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/blasto_comparative/proteins/')
files = [x for x in os.listdir() if x.endswith('oeli_less30.acc')]
database = '/Users/kika/ownCloud/blasto_comparative/proteins/CDS_problematic/Oeli_proteins_annotated.CDS_OK.fa'

for accessions in files: 
	print(accessions)
	fname = accessions.split('_less30.acc')[0]
	retrieve = set()

	with open('{}_proteins_annotated.CDS_OK_l30.fa'.format(fname), 'w') as out:
		db = SeqIO.parse(database, 'fasta')
		# print(db)
		for line in open(accessions):
			retrieve.add(line[:-1])
		# print(retrieve)
		for seq in db:
			if seq.name in retrieve:
				# print(seq.name)
				# out.write('>{}\n{}\n'.format(seq.description, seq.seq))
				pass
			else:
				# pass
				out.write('>{}\n{}\n'.format(seq.description, seq.seq))

