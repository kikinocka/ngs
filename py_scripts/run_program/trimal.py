#!/usr/bin/env python3
import os

os.chdir('/home/kika/ownCloud/SAGs/SSUs/ver6/')
files = [x for x in os.listdir() if 'mafft.aln' in x]

for file in files:
	print(file)
	file_name = file.split('_')[0] #+ '_' + file.split('_')[1]
	aut = 'automated1'
	gt = 0.75
	st = 0.001

	# output = '{}_trimal_{}.aln'.format(file_name, aut)
	# os.system('/home/kika/programs/trimAl/source/trimal -in {} -out {} -{} -fasta'.format(file, output, aut))
	
	output = '{}_trimal_{}.aln'.format(file_name, gt)
	os.system('/home/kika/programs/trimAl/source/trimal -in {} -out {} -gt {} -fasta'.format(file, output, gt))

	# output = '{}_trimal_{}_{}.aln'.format(file_name, gt, st)
	# os.system('/home/kika/programs/trimAl/source/trimal -in {} -out {} -gt {} -st {} -fasta'.format(file, output, gt, st))
