#!/usr/bin/python3
import os
from Bio import SeqIO

os.chdir('/home/kika/paratrypanosoma/')
genes = SeqIO.parse('orig_genes_now_corrupted.fasta', 'fasta')
out = open('orig_genes_codons.tsv', 'w')


for gene in genes:
	out.write('{}\t{}\t{}\n'.format(gene.description, gene.seq[0:3], gene.seq[len(gene.seq)-3:]))
out.close()