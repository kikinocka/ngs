#!/usr/bin/env python3
from Bio import SeqIO

infasta = SeqIO.parse('/home/kika/ownCloud/pelomyxa/transcriptome_assembly/pelomyxa_trinity_translated.fasta', 'fasta')
infile = open('/home/kika/ownCloud/pelomyxa/mito_proteins/import/tom-tim/hmm/in')
out = open('/home/kika/ownCloud/pelomyxa/mito_proteins/import/tom-tim/hmm/pelo_alphaMPP.hmm_hits.fa', 'w')

retrieve = set()
for line in infile:
	retrieve.add(line[:-1])

for seq in infasta:
	if seq.name in retrieve:
		out.write('>{}\n{}\n'.format(seq.description, seq.seq))
	else:
		print(seq.description)
out.close()