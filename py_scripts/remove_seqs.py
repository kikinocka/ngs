#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/pelomyxa_schiedti/ncbi_submission/transcriptome/')
remove = open('2-remove.txt')
fasta = SeqIO.parse('pelomyxa_transcriptome_clean.for_ncbi_without_adaptors.fa', 'fasta')

acc = set()
for line in remove:
	acc.add(line.strip())

with open('pelomyxa_transcriptome_clean.for_ncbi_without_adaptors_int-ex.fa', 'w') as out:
	for seq in fasta:
		if seq.name in acc:
			print(seq.name)
		else:
			out.write('>{}\n{}\n'.format(seq.description, seq.seq))
