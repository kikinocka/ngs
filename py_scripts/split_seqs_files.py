#!/usr/bin/env python3
import os
from Bio import SeqIO


os.chdir('/Users/kika/ownCloud/kinetoplastids/angomonas/')

for seq in SeqIO.parse('Adea_EAP.fasta', 'fasta'):
	with open('{}.fa'.format(seq.name.split('__')[0]), 'w') as result:
		result.write('>{}\n{}\n'.format(seq.description, seq.seq))
