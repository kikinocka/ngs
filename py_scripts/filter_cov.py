#!/usr/bin/python3
import os
from Bio import SeqIO

os.chdir('/home/kika/MEGAsync/diplonema_mt/1604/genome_assembly/')
genome = SeqIO.parse('1604_DNA_scaffolds.fasta', 'fasta')
table = open('1604_DNA_scaffolds_gc.tsv')

def get_cov(table):
	low = []
	for line in table:
		if 'contig' in line.split('\t')[0]:
			pass
		else:
			cov = float(line.split('\t')[0].split('_')[5])
			gc = float(line.split('\t')[7])
			if cov < 100:
				low.append(line.split('\t')[0])
	return low

low = get_gc_cov(table)
print(low)

with open('1604_DNA_scaffolds_filtered.fasta', 'w') as out:
	for contig in genome:
		if contig.name in low:
			pass
		else:
			out.write('>{}\n{}\n'.format(contig.description, contig.seq))