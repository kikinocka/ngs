#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/archamoebae/ribosomal_proteins/amoebae/alns_updated/renamed/')
files = [x for x in os.listdir() if x.endswith('.aln')]

with open('ribosomal_proteins.fa', 'w') as out:
	for file in files:
		file_name = file.split('.')[0]
		for seq in SeqIO.parse(file, 'fasta'):
			out.write('>{}__{}\n{}\n'.format(file_name, seq.name, str(seq.seq).replace('-', '')))
