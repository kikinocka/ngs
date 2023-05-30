#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/oil_sands/amplicons/18S-V4-2018/filtration/')
files = [x for x in os.listdir() if x.endswith('6.acc')]
database = '/Users/kika/ownCloud/oil_sands/amplicons/18S-V4-2018/filtration/check_cont.fa'

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
			if seq.name in retrieve:
				# out.write('>{}\n{}\n'.format(seq.description, seq.seq))
				pass
			else:
				# pass
				out.write('>{}\n{}\n'.format(seq.description, seq.seq))

