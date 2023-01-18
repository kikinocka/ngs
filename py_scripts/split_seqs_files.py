#!/usr/bin/env python3
import os
from Bio import SeqIO


os.chdir('/Users/kika/ownCloud/proteromonas/peroxisome/peroxins/')

for seq in SeqIO.parse('pram_peroxins.fa', 'fasta'):
	with open('{}.fa'.format(seq.name), 'w') as result:
		result.write('>{}\n{}\n'.format(seq.description, seq.seq))
