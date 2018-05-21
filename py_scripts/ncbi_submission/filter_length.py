#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/home/kika/MEGAsync/Data/EL_RNAseq/20140707_ver._r2013-02-05/')
transcriptome = SeqIO.parse('EL_merged_without_Ns_and_adapters.fsa', 'fasta')
result = open('EL_merged_without_Ns_and_adapters_longer200.fsa', 'w')

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