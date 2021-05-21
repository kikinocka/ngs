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
	print(line.strip().split('\t')[1])
	contig = line.split('\t')[0]
	start = line.split('\t')[1].split('..')[0]
	stop = line.strip().split('\t')[2].split('..')[0]
	primers[contig] = (start, stop)
print(primers)

# contigs = OrderedDict()
# for contig in transcriptome:
# 	contigs[contig.description] = contig.seq

# for key, value in contigs.items():
# 	if key in primers.keys():
# 		if primers[key][0] == 1:
# 			result.write('>{}\n{}\n'.format(key, value[primers[key][1]:]))
# 		else:
# 			result.write('>{}\n{}\n'.format(key, value[:primers[key][0]]))
# 	else:
# 		result.write('>{}\n{}\n'.format(key, value))

# result.close()