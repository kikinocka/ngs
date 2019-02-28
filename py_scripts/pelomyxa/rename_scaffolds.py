#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/home/kika/ownCloud/pelomyxa/genome_assembly/')
infa = SeqIO.parse('pelomyxa_clean_p-rna-scaffolder.fa', 'fasta')
outfa = open('pelomyxa_final.fa', 'w')

#the scaffold number and size, separated by a dash

c = 0
for seq in infa:
	l = len(seq.seq)
	c += 1
	outfa.write('>scaffold{}_{}\n{}\n'.format(c, l, seq.seq))

outfa.close()
