#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/home/kika/MEGAsync/Data/EL_RNAseq/20140707_ver._r2013-02-05/')
transcriptome = SeqIO.parse('EL_merged.fasta', 'fasta')
result = open('EL_merged_withoutNs.fsa', 'w')

for contig in transcriptome:
	print(contig.description)
	if str(contig.seq).startswith('N'):
		pos = str(contig.seq).rfind('N')
		result.write('>{}\n{}\n'.format(contig.description, contig.seq[pos+1:]))
	elif str(contig.seq).endswith('N'):
		pos = str(contig.seq).find('N')
		result.write('>{}\n{}\n'.format(contig.description, contig.seq[:pos]))
	else:
		result.write('>{}\n{}\n'.format(contig.description, contig.seq))