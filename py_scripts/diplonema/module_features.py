#!/usr/bin/env python3
import os

os.chdir('/home/kika/MEGAsync/diplonema_mt/1604/transcripts/gff/separate/')
files = sorted(os.listdir())
out = open('1604_genes_stats.tsv', 'w')

out.write('Gene\tNo. of modules\tA-to-I\tC-to-U\tNo. of SNPs\tU-appendage (length)\n')

for file in files:
	if file.endswith('.gff'):
		print(file)
		gene = file.split('_')[0]
		A_to_I = 0
		C_to_T = 0
		SNP = 0
		U_length = []
		for line in open(file):
			if line.split('\t')[2] == 'exon':
				modules = line.split('\t')[8].split('-m')[1][:-1]
			elif line.split('\t')[2] == 'misc_difference':
				if 'A>G' in line.split('\t')[8]:
					A_to_I += 1
				if 'C>T' in line.split('\t')[8]:
					C_to_T += 1
			elif line.split('\t')[2] == 'polymorphism' or line.split('\t')[2] == 'SNP':
				SNP += 1
			elif line.split('\t')[2] == 'poly-u':
				U_length.append(line.split('\t')[8].split('-pU')[1][:-1])
		out.write('{}\t{}\t{}\t{}\t{}\t{} ({})\n'.format(gene, modules, A_to_I, C_to_T, SNP, len(U_length),
			str(U_length).replace('\'', '').replace('[', '').replace(']', '')))

out.close()
