#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/home/kika/ownCloud/pelomyxa/transcriptome_assembly/stat/')
transcripts = SeqIO.parse('pelo_cegma.cegma.dna', 'fasta')
gff = open('pelo_cegma.cegma.gff')
plus = open('pelo_cegma_plus.dna', 'w')
minus = open('pelo_cegma_minus_RC.dna', 'w')

pairs = {}
for line in gff:
	kog = line.split('\t')[8][:-1]
	trin = line.split('\t')[0]
	strand = line.split('\t')[6]
	pairs[kog] = (trin, strand)

for transcript in transcripts:
	if transcript.name in pairs:
		if pairs[transcript.name][1] == '+':
			plus.write('>{} {}\n{}\n'.format(pairs[transcript.name][0], transcript.name, transcript.seq))
		else:
			minus.write('>{} {}\n{}\n'.format(pairs[transcript.name][0], transcript.name, transcript.seq.reverse_complement()))
	else:
		print(transcript.name)