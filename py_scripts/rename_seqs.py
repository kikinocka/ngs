#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/archamoebae/DNA_maintenance/replisome_amoebae/alns_updated/')
files = [x for x in os.listdir() if x.endswith('.aln')]

with open('replisome_proteins.fa', 'w') as out:
	for file in files:
		file_name = file.split('_')[0]
		for seq in SeqIO.parse(file, 'fasta'):
			if 'Homo' in seq.name or 'Dictyostelium' in seq.name:
				pass
			else:
				out.write('>{}__{}\n{}\n'.format(file_name, seq.name, str(seq.seq).replace('-', '')))
