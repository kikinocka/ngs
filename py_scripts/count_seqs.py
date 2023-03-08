#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Dcko/ownCloud/SAGs/phylogenomics/concatenated/ver2/')
alignments = [x for x in os.listdir() if x.endswith('.aln')]

counts = dict()
for aln in alignments:
	for seq in SeqIO.parse(aln, 'fasta'):
		if seq.name not in counts:
			counts[seq.name] = 1
		else:
			counts[seq.name] += 1

with open('taxa_counts.txt', 'w') as out:
	for key, value in counts.items():
		out.write('{}\t{}\n'.format(key, value))


# #COUNT HEADERS
# file = SeqIO.parse('/Users/kika/ownCloud/Gln-tRNA/stop-tRNAs/stop-CTA-tRNAs.fa', 'fasta')

# names = {}
# for seq in file:
# 	if seq.name not in names:
# 		names[seq.name] = 1
# 	else:
# 		names[seq.name] += 1

# print(names)