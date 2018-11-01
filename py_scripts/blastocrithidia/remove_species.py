#!/usr/bin/python3
import os
from Bio import SeqIO

os.chdir('/media/4TB1/blastocrithidia/orthofinder/sg_ogs/alignments/jac_renamed')
files = sorted(os.listdir())

for file in files:
	if file.endswith('_renamed.aln'):
		print(file)
		file_name = file.split('_')[0]
		out = open('/media/4TB1/blastocrithidia/seqfire/dataset/{}.fa'.format(file_name), 'w')
		for seq in SeqIO.parse(file, 'fasta'):
			if 'Bsal' in seq.name or 'Tbor' in seq.name or 'Linf' in seq.name:
				pass
			else:
				out.write('>{}\n{}\n'.format(seq.description, str(seq.seq).replace('-', '')))
