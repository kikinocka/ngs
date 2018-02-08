#!/usr/bin/python3
import os
from Bio import SeqIO

os.chdir('/home/kika/MEGAsync/blasto_project/predited_proteins/')
proteins = SeqIO.parse('p57_annotation_peptides_renamed.fasta', 'fasta')

with open('p57_fused_genes.fa', 'w') as out:
	for protein in proteins:
		if 'fused' in protein.description:
			out.write('>{}\n{}\n'.format(protein.description, protein.seq))
		else:
			pass