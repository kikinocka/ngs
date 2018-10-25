#!/usr/bin/env python3
import os
from collections import OrderedDict
from statistics import mean, median

os.chdir('/home/kika/MEGAsync/diplonema_mt/1610/transcripts/gff/')
files = sorted(os.listdir())
out = open('1610_module_sizes.tsv', 'w')

out.write('Modul\tLength\n')

modules_len = OrderedDict()
num_modules = 0
all_len = []
for file in files:
	if file.endswith('.gff'):
		print(file)
		gene = file.split('_')[0]
		for line in open(file):
			if line.split('\t')[2] == 'exon':
				start = int(line.split('\t')[3])
				end = int(line.split('\t')[4])
				length = end - start + 1
				num_modules += 1
				all_len.append(length)
				all_len = sorted(all_len)
				out.write('{}\t{}\n'.format(line.split('\t')[8].split('ID=')[1][:-1], length))

out.write('\nAverage module size\tMedian module size\tNumber of modules\n')
out.write('{}\t{}\t{}\n'.format(mean(all_len), median(all_len), num_modules))
out.close()
