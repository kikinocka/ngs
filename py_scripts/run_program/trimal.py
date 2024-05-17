#!/usr/bin/env python3
import os

trimal = '/Users/kika/miniconda3/bin/trimal'

os.chdir('/Users/kika/ownCloud/blasto_comparative/genes/catalase/')
files = [x for x in os.listdir() if x.endswith('.mafft.aln')]
# files = [x for x in os.listdir() if x.endswith('.einsi.aln')]

for file in files:
	print(file)
	# file_name = file.split('.')[0] + '.' + file.split('.')[1]
	file_name = file.split('.')[0]
	aut = 'automated1'
	gappyout = 'gappyout'
	gt = 0.8 #fraction of sequences with a gap allowed
	cons = 50 #minimum percentage of positions in the original alignment to conserve
	st = 0.001 #minimum average similarity allowed

	# output = '{}.trimal_{}.aln'.format(file_name, aut)
	# os.system('{} -in {} -out {} -{} -fasta'.format(trimal, file, output, aut))
	
	output = '{}.trimal_gt-{}.aln'.format(file_name, gt)
	os.system('{} -in {} -out {} -gt {} -fasta'.format(trimal, file, output, gt))

	# output = '{}.trimal_gt-{}_cons-{}.aln'.format(file_name, gt, cons)
	# os.system('{} -in {} -out {} -gt {} -cons {} -fasta'.format(trimal, file, output, gt, cons))

	# output = '{}.trimal_gt_{}_st_{}.aln'.format(file_name, gt, st)
	# os.system('{} -in {} -out {} -gt {} -st {} -fasta'.format(trimal, file, output, gt, st))
