#!/usr/bin/python3
import os
from Bio import SeqIO
from collections import OrderedDict

os.chdir('/home/kika/paratrypanosoma/')
genome = SeqIO.parse('paratryp_new.fa', 'fasta')
gff = open('result_renamed_lengths_no_split.gff', 'r')
out = open('paratryp_genes.fa', 'w')

def parse_gff(gff):
	coordinates = OrderedDict()
	for row in gff:
		if row.startswith('##'):
			pass
		else:
			seqid = row.split('\t')[0]
			start = int(row.split('\t')[3])
			end = int(row.split('\t')[4])
			strand = row.split('\t')[6]
			attributes = row.split('\t')[8].split('ID=')[1].split(';')[0]
			coordinates[attributes] = [start, end, seqid, strand]
	return coordinates

coordinates = parse_gff(gff)

contigs = OrderedDict()
for sequence in genome:
	contigs[sequence.description] = sequence.seq

for key, value in coordinates.items():
	if value[2] in contigs:
		if value[3] == '+':
			sequence = contigs[value[2]][value[0]-1:value[1]]
		else:
			sequence = contigs[value[2]][value[0]-1:value[1]].reverse_complement()
		out.write('>{}_{}\n{}\n'.format(key, value[2], sequence))
	else:
		print(value[2] + '_____no')
out.close()