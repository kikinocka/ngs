#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/membrane-trafficking/ARFs_ASR/Mandeep/FinalAlignmentused_for_ASR+Carpe6/With_Carpe/')
aln = SeqIO.parse('combinedArfs.fas', 'fasta')
out = 'Arfs.residues.tsv'

with open(out, 'w') as result:
	result.write('sequence\tlast 5 aa\n')
	for seq in aln:
		result.write('{}\t{}\n'.format(seq.name, seq.seq[-5:]))



# #clathrin
# with open(out, 'w') as result:
# 	result.write('sequence\tK108/105\tK130/127\tK141/138\n')
# 	for seq in aln:
# 		pos_1 = seq.seq[399]
# 		pos_2 = seq.seq[421]
# 		pos_3 = seq.seq[432]
# 		result.write('{}\t{}\t{}\t{}\n'.format(seq.name, pos_1, pos_2, pos_3))


# #CHC
# LYSK [1766]
# LEFK [1861]

# #CLC
# [399]
# [421]
# [432]