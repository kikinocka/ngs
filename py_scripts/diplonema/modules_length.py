#!/usr/bin/env python3
import os
from collections import OrderedDict
from statistics import mean, median

os.chdir('/home/kika/MEGAsync/diplonema_mt/1621/transcripts/gff/')
files = sorted(os.listdir())
out = open('1621_module_sizes.tsv', 'w')

out.write('Modul\tLength\n')

all_mod = OrderedDict()
num_modules = 0
all_len = []
for file in files:
	if file.endswith('.gff'):
		print(file)
		gene = file.split('_')[0]
		gene_mod = []
		utrs = [0, 0]
		for line in open(file):
			start = int(line.split('\t')[3])
			end = int(line.split('\t')[4])
			length = end - start + 1
			if line.split('\t')[2] == '5\'UTR':
				utrs[0] = length
			if line.split('\t')[2] == '3\'UTR':
				utrs[1] = length
			if line.split('\t')[2] == 'exon':
				gene_mod.append(length)
				num_modules += 1
				all_len.append(length)
				all_len = sorted(all_len)
		gene_mod[0] += utrs[0]
		gene_mod[-1] += utrs[1]
		for i in gene_mod:
			index = gene_mod.index(i) + 1
			module = '{}-m{}'.format(gene, str(index))
			out.write('{}\t{}\n'.format(module, i))

out.write('\nAverage module size\tMedian module size\tNumber of modules\n')
out.write('{}\t{}\t{}\n'.format(mean(all_len), median(all_len), num_modules))
out.close()
