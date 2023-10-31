#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/archamoebae/')
genome = SeqIO.parse('rhizomastix_libera_reassembly-IND8-VAV/rhizomastix_reassembly.trinity.fa', 'fasta')

with open('ncbi_submission/rlib.trinity_forNCBI.l200.fa', 'w') as out:
	for seq in genome:
		if len(seq) >= 200:
			out.write('>{}\n{}\n'.format(seq.description, seq.seq))
		else:
			print(seq.description)
