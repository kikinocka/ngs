#!/usr/bin/python3
import os
from Bio import SeqIO
from statistics import median

os.chdir('/home/kika/tara/')
sequences = SeqIO.parse('circular_CENJ01.fa', 'fasta')

lenghts = []
for seq in sequences:
	lenghts.append(len(seq.seq))

print(median(sorted(lenghts)))