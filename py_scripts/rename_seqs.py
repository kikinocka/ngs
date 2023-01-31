#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/blastocrithidia/predicted_proteins/')
proteins = SeqIO.parse('bnonstop_predicted_proteins.fasta', 'fasta')
table = open('bnonstop_func_annot.tsv')

annotation = {}
for line in table:
	accession = line.split('\t')[0].split(' ')[0]
	try:
		annot = ' | ' + line.split('\t')[3].split('|')[4].split('=')[1].strip() + ' | homolog of ' + line.split('\t')[3].split('|')[2].split('=')[1].strip()
	except:
		annot = ' | hypothetical protein'
	annotation[accession] = annot

with open('bnonstop_proteins_annotated.fa', 'w') as out:
	for seq in proteins:		
		out.write('>{}{}\n{}\n'.format(seq.name, annotation[seq.name], seq.seq))
