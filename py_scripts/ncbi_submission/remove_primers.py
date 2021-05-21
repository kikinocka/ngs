#!/usr/bin/env python3
import os
from Bio import SeqIO
from collections import OrderedDict

os.chdir('/Users/kika/ownCloud/pelomyxa_schiedti/ncbi_submission/transcriptome/')
contamination = open('to_trim.txt')
transcriptome = SeqIO.parse('pelomyxa_transcriptome_clean.for_ncbi.fa', 'fasta')
result = open('pelomyxa_transcriptome_clean.for_ncbi_without_adaptors.fa', 'w')

primers = {}
for line in contamination:
	contig = line.strip().split('\t')[0]
	start = int(line.strip().split('\t')[1].split('..')[0])
	stop = int(line.strip().split('\t')[1].split('..')[1])
	primers[contig] = (start, stop)

contigs = OrderedDict()
for contig in transcriptome:
	contigs[contig.name] = contig.seq


for key, value in contigs.items():
	if key in primers.keys():
		if primers[key][0] == 1:
			result.write('>{}\n{}\n'.format(key, value[primers[key][1]:]))
		elif primers[key][1] == len(value):
			 result.write('>{}\n{}\n'.format(key, value[:primers[key][0]]))
		# elif primers[key][1] < len(value)/2:
		# 	print(key)
		# 	print(value)
		# 	print(primers[key])
		# 	print(len(value), len(value)/2)
		# 	print(value[primers[key][1]:])
		else:
			result.write('>{}\n{}\n'.format(key, value))
	else:
		result.write('>{}\n{}\n'.format(key, value))

result.close()
