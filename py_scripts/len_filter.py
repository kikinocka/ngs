#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/mnt/data/kika/blastocrithidia/b_spHR05/scaff_gap/')
genome = SeqIO.parse('Braa.platanus_rnd1_scaffold.fa', 'fasta')

with open('Braa.platanus_rnd1_scaffold.l500.fa', 'w') as out:
	for seq in genome:
		if len(seq) >= 500:
			out.write('>{}\n{}\n'.format(seq.description, seq.seq))
		else:
			pass
