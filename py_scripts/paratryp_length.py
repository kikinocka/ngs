#!/usr/bin/python3
import os
from Bio import SeqIO

os.chdir('/home/kika/paratrypanosoma/')
fasta = SeqIO.parse('paratryp_new.fa', 'fasta')
out = open('lengths_trimmed_adaptors.tsv', 'w')

for sequence in fasta:
	out.write('{}\t{}\n'.format(sequence.description, len(sequence.seq)))
out.close()