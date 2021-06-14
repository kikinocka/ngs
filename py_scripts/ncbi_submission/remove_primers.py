#!/usr/bin/env python3
import os
from Bio import SeqIO
from collections import OrderedDict

os.chdir('/Users/kika/ownCloud/rhabdomonas_costata/ncbi_submission/')
contamination = open('3-to_trim.txt') #contig_name \t \d+..\d+
transcriptome = SeqIO.parse('Rhabdomonas_costata_transcriptome-20110611renamed.without_adaptors2_longer200-2_cont-removed.fa', 'fasta')
result = open('Rhabdomonas_costata_transcriptome-20110611renamed.without_adaptors3_cont-removed.fa', 'w')

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
		if primers[key][0] <= 10:
			result.write('>{}\n{}\n'.format(key, value[primers[key][1]:]))
		elif primers[key][1] >= len(value)-10:
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
