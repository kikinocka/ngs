#!/usr/bin/env python3
import os
from Bio import SeqIO, Entrez
from Bio.Blast import NCBIWWW

Entrez.email = 'zahonova.kristina@gmail.com'

os.chdir('/home/kika/ownCloud/pelomyxa/mito_proteins/chaperones/')
infile = SeqIO.parse('pelo_Hsp70.hmm_hits.fa', 'fasta')
out_handle = open('pelo_Hsp70_blast.txt', 'w')

for seq in infile:
	print(seq.name)
	result_handle = NCBIWWW.qblast('blastp', 'nr', '{}'.format(seq.seq))
	print('--------------------------')
	out_handle.write(result_handle.read())

out_handle.close()