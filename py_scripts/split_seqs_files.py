#!/usr/bin/env python3
import os
from Bio import SeqIO


os.chdir('/Users/kika/ownCloud/membrane-trafficking/queries/patchy_jotnarlogs/discoba/')

for seq in SeqIO.parse('queries.fa', 'fasta'):
	with open('{}_query.faa'.format(seq.name), 'w') as result:
		# print(str(result))
		result.write('>{}\n{}\n'.format(seq.description, seq.seq))
