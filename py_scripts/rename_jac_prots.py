#!/usr/bin/python3
import os
from Bio import SeqIO

os.chdir('/home/kika/MEGAsync/blasto_project/predited_proteins/')
table = open('jac_transc_prot_best_blast.tsv')

with open('jac_proteins_companion_renamed.fasta', 'w') as result:
	for line in table:
		proteins = SeqIO.parse('jac_proteins_companion.fasta', 'fasta')
		if line.split('\t')[0] == 'qseqid':
			pass
		else:
			for protein in proteins:
				if protein.description == line.split('\t')[0]:
					print(protein.description)
					first = protein.description.split(' ')[0]
					second = protein.description.split('_')[1]
					result.write('>{}__{}__{}\n{}\n'.format(first, 
						line.split('\t')[2].replace('***no hit found***', 'NO'), second, protein.seq))