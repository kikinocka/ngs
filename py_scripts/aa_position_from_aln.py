#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/membrane-trafficking/clathrin/')
aln = SeqIO.parse('CLC.mafft.aln', 'fasta')
out = 'CLC.residues.tsv'

# with open(out, 'w') as result:
# 	result.write('sequence\tlast 5 aa\n')
# 	for seq in aln:
# 		result.write('{}\t{}\n'.format(seq.name, seq.seq[-5:]))



#clathrin
with open(out, 'w') as result:
	# result.write('sequence\tK1326\tK1415\n')
	result.write('sequence\tW108/105\tW130/127\tW141/138\n')
	for seq in aln:
		pos_1 = seq.seq[889]
		pos_2 = seq.seq[946]
		pos_3 = seq.seq[957]
		# result.write('{}\t{}\t{}\n'.format(seq.name, pos_1, pos_2))
		result.write('{}\t{}\t{}\t{}\n'.format(seq.name, pos_1, pos_2, pos_3))


# CHC residues
# LYSK
# LEFK

# CLC residues
# IRKW
# EAEW
# LEEW
