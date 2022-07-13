#!/usr/bin/env python3
import os
from Bio import SeqIO


os.chdir('/Users/kika/ownCloud/archamoebae/import/HMMs-amoebozoa/')

for seq in SeqIO.parse('acas.fa', 'fasta'):
	with open('{}.fa'.format(seq.name), 'w') as result:
		result.write('>{}\n{}\n'.format(seq.description, seq.seq))
