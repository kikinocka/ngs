#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/home/kika/ownCloud/pelomyxa/augustus_training_set/')
fasta = SeqIO.parse('pelo_trinity_mbal_aa_dedupl.fa', 'fasta')
out = open('pelo_trinity_mbal_aa_final.fa', 'w')

pseudo = 0
incompl = 0
for seq in fasta:
	# print(seq.name, seq.seq[0])
	if 'X' in seq.seq:
		pseudo += 1
	elif 'M' != seq.seq[0]:
		incompl += 1
	else:
		out.write('>{}\n{}\n'.format(seq.description, str(seq.seq)))

print('pseudogenes: ' + str(pseudo))
print('truncated: ' + str(incompl))

out.close()