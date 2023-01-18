#!/usr/bin/python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/kinetoplastids/mito/')
infile = SeqIO.parse('M94286.1_genes.fa', 'fasta')
out = open('M94286.1_genes.start_codons.txt', 'w')

# #stops
# taa = 0
# tag = 0
# tga = 0
# other = 0

#starts
starts = {}

for sequence in infile:
	# #stops
	# full_seq = sequence.seq
	# seq = sequence.seq[-3:]
	# name = sequence.name
	# if seq == 'taa':
		# taa += 1
	# elif seq == 'tag':
		# tag += 1
	# elif seq == 'tga':
		# tga += 1
	# else:
		# other += 1
		# out_seqs.write('>{}\n{}\n'.format(name, full_seq))

	#starts
	if sequence.seq[0:3] not in starts:
		starts[sequence.seq[0:3]] = 1
	else:
		starts[sequence.seq[0:3]] += 1

for key, value in starts.items():
	out.write('{}: {}\n'.format(key, value))
