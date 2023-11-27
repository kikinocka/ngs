#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/oil_sands/metagenomes/')
genome = SeqIO.parse('20210222_BML-P3B/2-spades/P3B_scaffolds.fasta', 'fasta')

with open('ncbi_submission/P3B_NCBI.l200.fa', 'w') as out:
	for seq in genome:
		if len(seq) >= 200:
			out.write('>{}\n{}\n'.format(seq.description, seq.seq))
		else:
			print(seq.description)
