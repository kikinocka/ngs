#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/home/kika/MEGAsync/Data/EL_RNAseq/20140707_ver._r2013-02-05/')
contamination = open('NCBI_submission/report_upd.txt')
transcriptome = SeqIO.parse('EL_merged_withoutNs_longer200.fsa', 'fasta')
result = open('EL_merged_withoutNs_longer200_without_primers.fsa', 'w')

primers = {}
for line in contamination:
	contig = line.split('\t')[0]
	start = int(line.split('\t')[1])
	stop = int(line.split('\t')[2][:-1])
	primers[contig] = (start, stop)

for key, value in primers.items():
	for contig in transcriptome:
		print(contig.description)
		if key == contig.description:
			result.write('>{}\n{}\n'.format(key, contig.seq[:value[0]]))
		else:
			result.write('>{}\n{}\n'.format(contig.description, contig.seq))

result.close()