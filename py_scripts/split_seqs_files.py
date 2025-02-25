#!/usr/bin/env python3
import os
from Bio import SeqIO


os.chdir('/Users/kika/ownCloud/kinetoplastids/His_degradation/')

for seq in SeqIO.parse('Tcru_His_deg.fa', 'fasta'):
	with open('{}.faa'.format(seq.name.split('-')[0]), 'w') as result:
		result.write('>{}\n{}\n'.format(seq.description, seq.seq))
