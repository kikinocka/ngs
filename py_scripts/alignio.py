#!/usr/bin/env python3
import os
from Bio import SeqIO
from Bio import AlignIO

os.chdir('/Users/kika/ownCloud/membrane-trafficking/clathrin//')
# files = [x for x in os.listdir() if x.endswith('mafft.aln')]
aln = SeqIO.parse('CLC_opisthokonta.mafft.aln', 'fasta')
out = 'CLC_opisthokonta.residues.tsv'

# #number of sequences
# print(len(alignment))

# with open(out, 'w') as result:
# 	for file in files:
# 		print(file)
# 		# name = file.split('.')[0]
# 		aln = AlignIO.read(file, 'fasta')
# 		#number of positions
# 		# result.write('{}\t{}\n'.format(name, aln.get_alignment_length()))
# 		result.write('{}\t{}\n'.format(file, aln.get_alignment_length()))

with open(out, 'w') as result:
	result.write('sequence\tK108/105\tK130/127\tK141/138\n')
	for seq in aln:
		pos_1 = seq.seq[399]
		pos_2 = seq.seq[421]
		pos_3 = seq.seq[432]
		result.write('{}\t{}\t{}\t{}\n'.format(seq.name, pos_1, pos_2, pos_3))
