#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/blasto_comparative/proteins/')
genome = SeqIO.parse('Oeli_companion.CDS_cdseq_OK.fna', 'fasta')

with open('Oeli_companion.CDS_cdseq_OK_l30.fna', 'w') as out:
	for seq in genome:
		if len(seq) >= 90:
			out.write('>{}\n{}\n'.format(seq.description, seq.seq))
		else:
			print(seq.description)
