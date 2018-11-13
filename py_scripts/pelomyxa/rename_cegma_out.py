#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/home/kika/ownCloud/pelomyxa/genome_assembly/cegma/')
dna_seqs = SeqIO.parse('p1_cegma.cegma.dna', 'fasta')
gff = open('p1_cegma.cegma.gff')
plus = open('p1_cegma_plus.dna', 'w')
minus = open('p1_cegma_minus_RC.dna', 'w')

pairs = {}
for line in gff:
	kog = line.split('\t')[8][:-1]
	trin = line.split('\t')[0]
	strand = line.split('\t')[6]
	pairs[kog] = (trin, strand)

for dna_seq in dna_seqs:
	if dna_seq.name in pairs:
		if pairs[dna_seq.name][1] == '+':
			plus.write('>{} {}\n{}\n'.format(pairs[dna_seq.name][0], dna_seq.name, dna_seq.seq))
		else:
			minus.write('>{} {}\n{}\n'.format(pairs[dna_seq.name][0], dna_seq.name, dna_seq.seq.reverse_complement()))
	else:
		print(dna_seq.name)