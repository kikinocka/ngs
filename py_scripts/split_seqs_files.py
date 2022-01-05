#!/usr/bin/env python3
import os
from Bio import SeqIO


os.chdir('/Users/kika/ownCloud/archamoebae/ribosomal_proteins/')
seqs = SeqIO.parse('ehis.fa', 'fasta')

for seq in seqs:
	with open('amoebae/{}.faa'.format(seq.name), 'w') as result:
		result.write('>{}\n{}\n'.format(seq.description, seq.seq))
