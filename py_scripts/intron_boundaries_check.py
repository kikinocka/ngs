#!/usr/bin/env python3
import os
from Bio import SeqIO
from collections import Counter

os.chdir('/Users/kika/ownCloud/archamoebae/mastigamoeba_balamuthi/Masba_gff3_LATEST/')
introns = SeqIO.parse('masba_introns_final.fa', 'fasta')
outfile = 'masba_intron_counts.txt'

starts = []
ends = []
boundaries = []
for intron in introns:
	start = str(intron.seq[:2])
	end = str(intron.seq[-2:])
	boundaries.append(start+end)
	starts.append(start)
	ends.append(end)

with open(outfile, 'w') as out:

	out.write('Intron boundaries\n')
	for i, c in Counter(boundaries).items():
		out.write('{}-{}:\t{}\n'.format(i[:2], i[-2:], c))
	out.write('*************\n\n')

	# out.write('Intron starts\n')
	# for i, c in Counter(starts).items():
	# 	out.write('{}:\t{}\n'.format(i, c))
	# out.write('*************\n\n')

	# out.write('Intron ends\n')
	# for i, c in Counter(ends).items():
	# 	out.write('{}:\t{}\n'.format(i, c))
	# out.write('*************\n')
