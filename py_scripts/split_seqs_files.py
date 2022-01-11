#!/usr/bin/env python3
import os
from Bio import SeqIO


os.chdir('/Users/kika/ownCloud/archamoebae/DNA_maintenance/replisome_amoebae/')
seqs = SeqIO.parse('replisome.fa', 'fasta')

for seq in seqs:
	with open('{}.faa'.format(seq.name), 'w') as result:
		result.write('>{}\n{}\n'.format(seq.description, seq.seq))
