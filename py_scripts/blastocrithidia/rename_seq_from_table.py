#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/home/kika/MEGAsync/blasto_project/ku_story/alignments/')
fasta = SeqIO.parse('ku80_reduced.fa', 'fasta')
taxonomy = open('taxonomy.tsv')
out = open('ku80_reduced_renamed.fa', 'w')

taxid = {}
for line in taxonomy:
	if line.startswith('Taxid'):
		pass
	else:
		taxid[line.split('\t')[0]] = (line.split('\t')[1], line.split('\t')[2].split(',')[0], 
			line.split('\t')[2].split(',')[1])

for seq in fasta:
	seq_name = seq.name.split('.')[0]
	prot_id = seq.name.split('.')[1]
	if seq_name in taxid:
		out.write('>{} {} [{}, {}]\n{}\n'.format(taxid[seq_name][0], prot_id, taxid[seq_name][1], taxid[seq_name][2],
			seq.seq))
	else:
		print(seq_name + ' not found')

out.close()
