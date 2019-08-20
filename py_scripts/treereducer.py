#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/home/kika/ownCloud/euglenophytes/repair/photolyases/seqs/')
inacc = open('acc.delete.txt')
infasta = SeqIO.parse('photolyases_deduplicated.fa', 'fasta')

omitted = []
for line in inacc:
	omitted.append(line.strip())

with open('photolyases_reduced.fa', 'w') as result:
	for seq in infasta:
		if seq.name in omitted:
			print('{} in omitted list'.format(seq.name))
		else:
			result.write('>{}\n{}\n'.format(seq.description, seq.seq))
