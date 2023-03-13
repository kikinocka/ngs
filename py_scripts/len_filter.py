#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/blasto_comparative/proteins/companion/')
genome = SeqIO.parse('Ovol_companion.fa', 'fasta')

with open('Ovol_companion.l30.faa', 'w') as out:
	for seq in genome:
		if len(seq) >= 30:
			out.write('>{}\n{}\n'.format(seq.description, seq.seq))
		else:
			print(seq.description)
