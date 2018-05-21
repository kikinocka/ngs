#!/usr/bin/env python3
import os
from Bio import SeqIO

fastas = SeqIO.parse('all_aa.fasta', 'fasta')
with open('_table_to_fill_sequences.txt') as f:
	table = f.read().split('\n')

fastadict = {}
for contig in fastas:
	seqname = contig.name.split('_')[0].replace('-reversed', '')
	fastadict[seqname] = contig.seq

result = open('_table_with_filled_sequences.tsv', 'w')
for line in table:
	if 'Contig' in line:
		data = line.split('\t')
		contigID = data[1]
		#print(data)
		if data[2] == '+':
			line = line.replace('\t+\t', '\t\'+\t')
		contigseq = fastadict.get(contigID, 'not found')
		if contigseq == 'not found':
			print('{} needs to be added manually'.format(contigID))
			result.write('{}\tSEQUENCE NOT FOUND\n'.format(line))
		else:
			result.write('{}\t{}\n'.format(line, contigseq))
	else:
		result.write('{}\n'.format(line))
print('Finished.')