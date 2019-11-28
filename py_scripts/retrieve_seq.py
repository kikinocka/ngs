#!/usr/bin/python3
import os
from Bio import SeqIO

os.chdir('/home/kika/ownCloud/pelomyxa_schiedti/predicted_proteins_transdecoder/')
db = SeqIO.parse('pelo_transcriptome_clean.fa.transdecoder.5prime_complete.clustered.pep', 'fasta')
accessions = open('in')
out = open('possibly_interesting.fa', 'w')

retrieve = set()
for line in accessions:
	retrieve.add(line[:-1])

for seq in db:
	if seq.name in retrieve:
		out.write('>{}\n{}\n'.format(seq.name, seq.seq))
	else:
		# print(seq.description)
		pass
out.close()
