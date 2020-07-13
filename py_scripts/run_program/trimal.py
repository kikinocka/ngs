#!/usr/bin/env python3
import os

trimal = '/Users/kika/miniconda3/bin/trimal'

os.chdir('/Users/kika/ownCloud/SAGs/mit/nad11/ver1/')
files = [x for x in os.listdir() if 'mafft.aln' in x]

for file in files:
	print(file)
	file_name = file.split('.')[0] #+ '_' + file.split('_')[1]
	aut = 'automated1'
	gt = 0.5 #fraction of sequences with a gap allowed
	st = 0.001 #minimum average similarity allowed.

	# output = '{}.trimal_{}.aln'.format(file_name, aut)
	# os.system('{} -in {} -out {} -{} -fasta'.format(trimal, file, output, aut))
	
	output = '{}.trimal_gt_{}.aln'.format(file_name, gt)
	os.system('{} -in {} -out {} -gt {} -fasta'.format(trimal, file, output, gt))

	# output = '{}.trimal_gt_{}_st_{}.aln'.format(file_name, gt, st)
	# os.system('{} -in {} -out {} -gt {} -st {} -fasta'.format(
	# trimal, file, output, gt, st))
