#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/membrane-trafficking/diplonemids_all/trees/TBCs/')
files = [x for x in os.listdir() if x.endswith('.in')]
database = '/Users/kika/ownCloud/diplonema/seq_data/dpapillatum/representative_Ogar/dpap_transcripts_ed-minus_bac.fa'

for accessions in files: 
	print(accessions)
	fname = accessions.split('.in')[0]
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
				# out.write('>{}\n{}\n'.format(seq.description, seq.seq))
				pass

