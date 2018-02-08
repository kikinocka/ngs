#!/usr/bin/python3
import os
from Bio import SeqIO

os.chdir('/home/kika/MEGAsync/blasto_project/blast_searches/p57_fused_genes/')
genes = SeqIO.parse('p57_fused_genes.fa', 'fasta')
ms_blast = open('peptides_MS_best_blast.tsv')

def get_info(genes):
	info = {}
	for gene in genes:
		protein = gene.description.split(' ')[0]
		contig = gene.description.split(' ')[2]
		start = gene.description.split(' ')[3].split('-')[0]
		end = gene.description.split(' ')[3].split('-')[1]
		info[protein] = [contig, start, end]
	return info

