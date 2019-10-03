#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/home/kika/ownCloud/pelomyxa_schiedti/predicted_proteins/')
fasta = SeqIO.parse('pelo_transcriptome_clean.fa.transdecoder.5prime_complete.clustered.pep', 'fasta')
targetp = open('pelo_transcriptome_clean.fa.transdecoder.5prime_complete.clustered.targetp.txt')

names = {}
for seq in fasta:
	full = seq.name.split(':')[0]
	short = seq.name[:20]
	names[short] = full

with open('pelo_transcriptome_clean.fa.transdecoder.5prime_complete.clustered.targetp_renamed.txt', 'w') as out:
	for line in targetp:
		if line.split('\t')[0] in names:
			new = line.replace(line.split('\t')[0], names[line.split('\t')[0]])
			out.write(new)
