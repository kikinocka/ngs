#!/usr/bin/env python3
import os
from Bio import SeqIO


os.chdir('/Users/kika/ownCloud/proteromonas/flagellar/amoebae_stramenopiles/')

for seq in SeqIO.parse('queries.faa', 'fasta'):
	with open('{}.faa'.format(seq.name), 'w') as result:
		result.write('>{}\n{}\n'.format(seq.description, seq.seq))
