#!/usr/bin/env python3
import os
from Bio import SeqIO


os.chdir('/Users/kika/ownCloud/kinetoplastids/AOX/amoebae_etc/queries/')

for seq in SeqIO.parse('alt.fa', 'fasta'):
	with open('alt_{}.fa'.format(seq.name), 'w') as result:
		result.write('>{}\n{}\n'.format(seq.description, seq.seq))
