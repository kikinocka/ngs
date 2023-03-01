#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/archamoebae/rhizomastix_vacuolata/trinity-filt2/')
genome = SeqIO.parse('rvac.trinity.fasta', 'fasta')

with open('rvac.trinity_forNCBI.l200.fa', 'w') as out:
	for seq in genome:
		if len(seq) >= 200:
			out.write('>{}\n{}\n'.format(seq.description, seq.seq))
		else:
			print(seq.description)
