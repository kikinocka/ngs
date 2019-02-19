#!/usr/bin/env python3
import os

os.chdir('/home/kika/MEGAsync/diplonema_mt/1610/transcripts/gff/')
files = sorted(os.listdir())
out = open('1610_junctions.tsv', 'w')

for file in files:
	if file.endswith('.gff'):
		print(file)
		out.write('{}\n'.format(file.split('_')[0]))
		positions = []
		for line in open(file):
			if line.split('\t')[2] == 'exon':
				positions.append(int(line.split('\t')[3]))
				positions.append(int(line.split('\t')[4]))

		for i in range(len(positions)):
			if i+1 < len(positions):
				if positions[i] >= positions[i+1]:
					junction = positions[i] - positions[i+1] + 1
					first = int((i+1) / 2)
					second = first + 1
					out.write('m{}\tm{}\t{}\n'.format(first, second, junction))
out.close()
