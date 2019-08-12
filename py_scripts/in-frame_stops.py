#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/home/kika/pelomyxa_schiedti/pasa-evm/')
infasta = SeqIO.parse('pelomyxa_predicted_proteins.fa', 'fasta')

with open('pelomyxa_proteins_stops.fa', 'w') as stops; with open('pelomyxa_proteins_correct.fa', 'w') as good:
	for seq in infasta:
		if '.' in seq.seq:
			stops.write('>{}\n{}\n'.format(seq.description, seq.seq))
		else:
			good.write('>{}\n{}\n'.format(seq.description, seq.seq))
