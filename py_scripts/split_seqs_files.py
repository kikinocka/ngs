#!/usr/bin/env python3
import os
from Bio import SeqIO


os.chdir('/Users/kika/ownCloud/archamoebae/DNA_maintenance/')
seqs = SeqIO.parse('dna_maintenance.fasta', 'fasta')

for seq in seqs:
	with open('amoebae/{}.faa'.format(seq.name), 'w') as result:
		result.write('>{}\n{}\n'.format(seq.description, seq.seq))
