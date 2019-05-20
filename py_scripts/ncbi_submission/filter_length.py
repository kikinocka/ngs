#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/home/kika/ownCloud/blastocrithidia/genome_assembly/')
transcriptome = SeqIO.parse('jaculum_scaffolds.fasta', 'fasta')
result = open('jac_scaffolds_longer200.fa', 'w')

all_cont = 0
long_cont = 0
for contig in transcriptome:
	print(contig.description)
	all_cont += 1
	if len(contig.seq) < 200:
		pass
	else:
		long_cont += 1
		result.write('>{}\n{}\n'.format(contig.description, contig.seq))

print(all_cont)
print(long_cont)