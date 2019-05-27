#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/home/kika/ownCloud/blastocrithidia/genome_assembly/NCBI_submission/')
transcriptome = SeqIO.parse('jac_scaffolds_trimmed.fa', 'fasta')
result = open('jac_scaffolds_trimmed_without_Ns.fa', 'w')

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