#!/usr/bin/env python3
import os
from Bio import SeqIO

# os.chdir('/Users/kika/ownCloud/pelomyxa_schiedti/')
# remove = open('ncbi_submission/genome/remove.acc')
# fasta = SeqIO.parse('pasa-evm/pelomyxa_introns_final.fa', 'fasta')

# acc = set()
# for line in remove:
# 	acc.add(line.strip())

# with open('pasa-evm/pelomyxa_introns_final-removed.fa', 'w') as out:
# 	for seq in fasta:
# 		if seq.name in acc:
# 			print(seq.name)
# 		else:
# 			out.write('>{}\n{}\n'.format(seq.description, seq.seq))


os.chdir('/Users/kika/ownCloud/SL_Euglenozoa/V9/metamonada/')
infasta = SeqIO.parse('metamonads_eukref-otus.fa', 'fasta')

c = 0
with open('metamonads_eukref-otus.unambiguous.fa', 'w') as out:
	for seq in infasta:
		if ('N' in seq.seq.upper()) or \
		('U' in seq.seq.upper()) or \
		('W' in seq.seq.upper()) or \
		('S' in seq.seq.upper()) or \
		('M' in seq.seq.upper()) or \
		('K' in seq.seq.upper()) or \
		('R' in seq.seq.upper()) or \
		('Y' in seq.seq.upper()) or \
		('B' in seq.seq.upper()) or \
		('D' in seq.seq.upper()) or \
		('H' in seq.seq.upper()) or \
		('V' in seq.seq.upper()):
			c +=1
			print(seq.name)
		else:
			out.write('>{}\n{}\n'.format(seq.description, seq.seq))

print('ambiguous sequences: {}'.format(c))
