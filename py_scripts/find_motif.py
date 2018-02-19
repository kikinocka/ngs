#!/usr/bin/python3
import os
import re
from Bio import SeqIO

os.chdir('/home/kika/MEGAsync/blasto_project/fused_proteins/')
genes = SeqIO.parse('p57_fused_genes.fa', 'fasta')

for gene in genes:
	if re.search(r'D\wE\wNPGP', str(gene.seq)):
		print(gene.description)