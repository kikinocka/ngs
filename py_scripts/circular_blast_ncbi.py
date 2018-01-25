#!/usr/bin/python3
import os
from Bio import SeqIO
from Bio.Blast import NCBIWWW

infile = SeqIO.parse('/home/kika/tara/test/circulars.fa', 'fasta')
out_handle = open('/home/kika/tara/test/circulars_blast.txt', 'w')

for seq in infile:
	print(seq.name)
	result_handle = NCBIWWW.qblast('blastx', 'nr', '{}'.format(seq.seq))
	print('--------------------------')
	out_handle.write(result_handle.read())

out_handle.close()