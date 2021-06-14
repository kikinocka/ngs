#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/rhabdomonas_costata/ncbi_submission/')
remove = open('3-ncbi_report_contamination.txt')
fasta = SeqIO.parse('Rhabdomonas_costata_transcriptome-20110611renamed.without_adaptors2_longer200-2.fa', 'fasta')

acc = set()
for line in remove:
	acc.add(line.strip())

with open('Rhabdomonas_costata_transcriptome-20110611renamed.without_adaptors2_longer200-2_cont-removed.fa', 'w') as out:
	for seq in fasta:
		if seq.name in acc:
			print(seq.name)
		else:
			out.write('>{}\n{}\n'.format(seq.description, seq.seq))
