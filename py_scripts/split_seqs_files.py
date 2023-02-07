#!/usr/bin/env python3
import os
from Bio import SeqIO


os.chdir('/Users/kika/ownCloud/proteromonas/flagellar/amoebae_stramenopiles/')

for seq in SeqIO.parse('blasto_not-found.fa', 'fasta'):
	with open('{}.fa'.format(seq.name), 'w') as result:
		result.write('>{}\n{}\n'.format(seq.description, seq.seq))
