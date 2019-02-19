#!/usr/bin/env python3
import os

os.chdir('/home/kika/MEGAsync/Konferencie, seminare/2019 01 06-19 Genomics Cesky Krumlov/lectures/')
infile = open('reads.txt')
out = open('corrected_reads.fq', 'w')

seqs = []
for line in infile:
	if line.startswith('I') or line.startswith('+') or line.startswith('@'):
		pass
	else:
		seqs.append(line[:-1])
		
x = 3000 * 'I'
for i in range(len(seqs)):
	out.write('@{}\n{}\n+\n{}\n'.format(i, seqs[i], x))
