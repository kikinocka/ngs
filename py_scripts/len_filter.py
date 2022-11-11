#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/mnt/data/kika/blastocrithidia/o_volfi/scaff_gap/')
genome = SeqIO.parse('Ovol.platanus_rnd2_scaffold.fa', 'fasta')

with open('Ovol.platanus_rnd2_scaffold.l500.fa', 'w') as out:
	for seq in genome:
		if len(seq) >= 500:
			out.write('>{}\n{}\n'.format(seq.description, seq.seq))
		else:
			print(seq.description)
