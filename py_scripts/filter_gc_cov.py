#!/usr/bin/python3
import os
from Bio import SeqIO

os.chdir('/home/kika/MEGAsync/diplonema_mt/1604/genome_assembly/')
genome = SeqIO.parse('1604_DNA_scaffolds.fasta', 'fasta')
table = open('1604_DNA_scaffolds_gc.tsv')
out = open('1604_DNA_scaffolds_filtered.fasta', 'w')

def get_gc_cov(table):
	bkt = []
	for line in table:
		if 'contig' in line.split('\t')[0]:
			pass
		else:
			name = line.split('\t')[0]
			cov = float(line.split('\t')[0].split('_')[5])
			gc = float(line.split('\t')[7])
			if 28 <= gc <= 32 and cov < 100:
				bkt.append(line.split('\t')[0])
			elif cov < 100:
				bkt.append(line.split('\t')[0])
	return bkt

def filter_genome(genome, bkt):
	for contig in genome:
		if contig.name in bkt:
			pass
		else:
			out.write('>{}\n{}\n'.format(contig.description, contig.seq))

bkt = get_gc_cov(table)
print(bkt)
bla = filter_genome(genome, bkt)