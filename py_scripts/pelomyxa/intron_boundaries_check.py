#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/home/kika/ownCloud/pelomyxa/augustus_training_set/')
introns = SeqIO.parse('introns.fasta', 'fasta')

for intron in introns:
	beginning = intron.seq[:2]
	end = intron.seq[-2:]
	if beginning != 'GT':
		print(intron.name.split('_')[0], beginning)
	if end != 'AG':
		print(intron.name.split('_')[0], end)
