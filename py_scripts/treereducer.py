#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/kinetoplastids/kinesins/kinesins/kin2/')
inacc = open('kinesins.trimal_gt-0.8.marked.treefile')
infasta = SeqIO.parse('/Users/kika/ownCloud/kinetoplastids/kinesins/kinesins/kin_all_tree/ver2/kinesins.fa', 'fasta')

omitted = []
for line in inacc:
	if 'color=' in line:
		print(line.split('[')[0].replace('\'', '').replace('\t', ''))
	omitted.append(line.split('[')[0].replace('\'', '').replace('\t', ''))

c = 0
with open('kinesins.fa', 'w') as result:
	for seq in infasta:
		if seq.description in omitted:
			c += 1
			print('{} in omitted list'.format(seq.name))
		else:
			result.write('>{}\n{}\n'.format(seq.description, seq.seq))
print(c)
