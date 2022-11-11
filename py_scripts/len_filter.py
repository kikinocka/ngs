#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/mnt/data/kika/blastocrithidia/o_modryi/scaff_gap/')
genome = SeqIO.parse('Omod.platanus_rnd1_scaffold.fa', 'fasta')

with open('Omod.platanus_rnd1_scaffold.l500.fa', 'w') as out:
	for seq in genome:
		if len(seq) >= 500:
			out.write('>{}\n{}\n'.format(seq.description, seq.seq))
		else:
			print(seq.description)
