#!/usr/bin/python3
import os
from Bio import SeqIO
from collections import OrderedDict

os.chdir('/home/kika/paratrypanosoma/')
gff = open('result_renamed_lengths_no_split.gff', 'r')
genome = SeqIO.parse('paratryp_new.fa', 'fasta')
out = open('codons.tsv', 'w')

coordinates = OrderedDict()
for row in gff:
	if row.startswith('##'):
		pass
	else:
		coordinates[row.split('\t')[8].split('ID=')[1].split(';')[0]] = [row.split('\t')[0], int(row.split('\t')[3]),
			int(row.split('\t')[4]), row.split('\t')[6]]

for contig in genome:
	for key, value in coordinates.items():
		if contig.description == value[0]:
			if value[3] == '+':
				out.write('{}\t{}\t{}\n'.format(key, contig.seq[value[1]-1:value[1]+2], 
					contig.seq[value[2]-3:value[2]]))
			else:
				out.write('{}\t{}\t{}\n'.format(key, contig.seq[value[2]-3:value[2]].reverse_complement(),
					contig.seq[value[1]-1:value[1]+2].reverse_complement()))
out.close()