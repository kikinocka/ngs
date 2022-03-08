#!/usr/bin/env python3
import os
from Bio import SeqIO


os.chdir('/storage/brno3-cerit/home/kika/oil_sands/metagenomes/20200821_BML-P3B/')
db = SeqIO.parse('2a-spades_default/scaffolds.fasta', 'fasta')

with open('metabinner/scaffolds_len500.fa', 'w') as out:
	for seq in db:
		print(seq.name)
		if len(seq.seq) < 500:
			pass
		else:
			out.write('>{}\n{}\n'.format(seq.description, seq.seq))
