#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/oil_sands/metagenomes/20200821_BML-P3B/metabinner/')
metabinner = open('metabinner_result.tsv')
contigs = SeqIO.parse('scaffolds_len500.fa', 'fasta')

# cont_dict = {}
# for seq in contigs:
# 	cont_dict[seq.name] = seq.seq

# for line in metabinner:
# 	name = line.split('\t')[0]
# 	bin = line.split('\t')[1].strip()
# 	with open('bin_{}.fa'.format(bin), 'a') as out, open('unbinned.fa', 'a') as unclas:
# 		if name in cont_dict.keys():
# 			out.write('>{}\n{}\n'.format(name, cont_dict[name]))
# 		else:
# 			unclas.write('>{}\n{}\n'.format(name, cont_dict[name]))

meta_dict = {}
for line in metabinner:
	name = line.split('\t')[0]
	bin = line.split('\t')[1].strip()
	meta_dict[name] = bin

for seq in contigs:
	if seq.name in meta_dict.keys():
		with open('bin_{}.fa'.format(meta_dict[seq.name]), 'a') as out:
			out.write('>{}\n{}\n'.format(seq.name, seq.seq))
	else:
		with open('unbinned.fa', 'a') as unclas:
			unclas.write('>{}\n{}\n'.format(seq.name, seq.seq))
