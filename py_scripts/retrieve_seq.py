#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/home/kika/ownCloud/pelomyxa_schiedti/predicted_proteins_transdecoder/')
infasta = SeqIO.parse('pelo_transcriptome_clean.fa.transdecoder.5prime_complete.clustered.pep', 'fasta')
infile = open('mit.acc')
out = open('mit.predicted.fa', 'w')

retrieve = set()
for line in infile:
	retrieve.add(line[:-1])

for seq in infasta:
	if seq.name.split('::')[0] in retrieve:
		out.write('>{}\n{}\n'.format(seq.name.split('::')[0], seq.seq))
	else:
		# print(seq.description)
		pass
out.close()
