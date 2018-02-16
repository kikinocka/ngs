#!/usr/bin/python3
import os
from Bio import SeqIO

os.chdir('/home/kika/MEGAsync/diplonema_mt/1621/genome_assembly/')
genome = SeqIO.parse('1621_DNA_scaffolds.fasta', 'fasta')

def get_cov(genome):
	low = []
	for contig in genome:
		cov = float(contig.name.split('_')[-1])
		if cov < 100:
			low.append(contig.name)
	return low

low = get_cov(genome)
print(low)

genome = SeqIO.parse('1621_DNA_scaffolds.fasta', 'fasta')
with open('1621_DNA_scaffolds_filtered.fasta', 'w') as out:
	for contig in genome:
		if contig.name in low:
			pass
		else:
			out.write('>{}\n{}\n'.format(contig.description, contig.seq))