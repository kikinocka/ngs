#!/usr/bin/env python3
import os
from Bio import SeqIO


os.chdir('/media/4TB1/blastocrithidia/new_3-UTR/contextmap/Bn_split_genome/')
seqs = SeqIO.parse('/media/4TB1/blastocrithidia/genome_assembly/bnonstop_corrected_assembly.fasta', 'fasta')

for seq in seqs:
	with open('{}.fa'.format(seq.name), 'w') as result:
		result.write('>{}\n{}\n'.format(seq.description, seq.seq))
