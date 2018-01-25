#!/usr/bin/python3
import os
from Bio import SeqIO

proteins = SeqIO.parse('/home/kika/MEGAsync/Chlamydomonas/od_toma/putative_pt_genes_aa.fa', 'fasta')

with open('/home/kika/MEGAsync/Chlamydomonas/od_toma/putative_pt_genes_aa_complete5.fa', 'w') as complete:
	for protein in proteins:
		if '5prime' in protein.description:
			print(protein.description)
		else:
			complete.write('>{}\n{}\n'.format(protein.description, protein.seq))