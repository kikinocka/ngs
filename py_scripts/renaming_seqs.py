#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/data/stramenopiles/')
fasta = SeqIO.parse('incisomonas_marina.fa', 'fasta')

c = 0
with open('incisomonas_marina_renamed.fa', 'w') as out:
	for seq in fasta:
		c += 1
		out.write('>Imar_{}\n{}\n'.format(c, seq.seq))
