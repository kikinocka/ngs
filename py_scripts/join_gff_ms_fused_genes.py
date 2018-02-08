#!/usr/bin/python3
import os
from Bio import SeqIO

os.chdir('/home/kika/MEGAsync/blasto_project/blast_searches/p57_fused_genes/')
genes = SeqIO.parse('p57_fused_genes.fa', 'fasta')
ms_blast = open('peptides_MS_best_blast.tsv')
gff = open('p57_fused.gff')

def get_info(genes, gff):
	info = {}
	for gene in genes:
		protein = gene.description.split(' ')[0]
		contig = gene.description.split(' ')[2]
		uniqueid = gene.description.split(' ')[4].split(',')[0].split('ID=')[1]
		start = gene.description.split(' ')[3].split('-')[0]
		end = gene.description.split(' ')[3].split('-')[1]
		info[uniqueid] = [protein, contig, start, end]
	for line in gff:
		try:
			protid = line.split('\t')[8].split(';')[0].split('ID=')[1]
			strand = line.split('\t')[6]
			if protid in info.keys():
				info[protid].append(strand)
		except:
			pass
	return info

def parse_blast(ms_blast):
	blast = {}
	for line in ms_blast:
		try:
			protein = line.split('\t')[2]
			peptide = line.split('\t')[0]
			start = line.split('\t')[12]
			end = line.split('\t')[13]
			aln = float(line.split('\t')[14])
			if aln == 1:
				blast[protein] = [peptide, start, end]
		except:
			pass
	return blast

info = get_info(genes, gff)
blast = parse_blast(ms_blast)

