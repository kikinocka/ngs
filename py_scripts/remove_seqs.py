#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/pelomyxa_schiedti/')
remove = open('ncbi_submission/genome/remove.acc')
fasta = SeqIO.parse('pasa-evm/pelomyxa_introns_final.fa', 'fasta')

acc = set()
for line in remove:
	acc.add(line.strip())

with open('pasa-evm/pelomyxa_introns_final-removed.fa', 'w') as out:
	for seq in fasta:
		if seq.name in acc:
			print(seq.name)
		else:
			out.write('>{}\n{}\n'.format(seq.description, seq.seq))
