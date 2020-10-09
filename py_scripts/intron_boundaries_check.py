#!/usr/bin/env python3
import os
from Bio import SeqIO
from collections import Counter

os.chdir('/Users/kika/ownCloud/pelomyxa_schiedti/pasa-evm/')
introns = SeqIO.parse('pelomyxa_introns_final.fa', 'fasta')
outfile = 'pelomyxa_intron_counts.txt'

starts = []
ends = []
for intron in introns:
	starts.append(str(intron.seq[:2]))
	ends.append(str(intron.seq[-2:]))

with open(outfile, 'w') as out:
	out.write('Intron starts\n')
	for i, c in Counter(starts).items():
		out.write('{}:\t{}\n'.format(i, c))
	out.write('*************\n\n')
	out.write('Intron ends\n')
	for i, c in Counter(ends).items():
		out.write('{}:\t{}\n'.format(i, c))
	out.write('*************\n')
