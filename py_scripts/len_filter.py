#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/mnt/data/kika/blastocrithidia/b_triatomae/spades_75_karect/')
genome = SeqIO.parse('scaffolds.fasta', 'fasta')

with open('scaffolds.l500.fa', 'w') as out:
	for seq in genome:
		if len(seq) >= 500:
			out.write('>{}\n{}\n'.format(seq.description, seq.seq))
		else:
			pass
