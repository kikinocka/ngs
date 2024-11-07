#!/usr/bin/env python3
import os
from Bio import SeqIO


os.chdir('/Users/kika/ownCloud/membrane-trafficking/diplonemids_ESCRTs/ESCRT-0/amoebae/')

for seq in SeqIO.parse('vhs_gat_query.fa', 'fasta'):
	with open('queries/{}.faa'.format(seq.name), 'w') as result:
		result.write('>{}\n{}\n'.format(seq.description, seq.seq))
