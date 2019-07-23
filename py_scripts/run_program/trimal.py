#!/usr/bin/env python3
import os

os.chdir('/home/kika/ownCloud/pelomyxa_schiedti/mito_proteins/sulfate_activation/IPP_tree/')
files = [x for x in os.listdir() if 'MAFFT.aln' in x]

for file in files:
	print(file)
	file_name = file.split('_')[0] #+ '_' + file.split('_')[1]
	aut = 'automated1'
	gt = 0.5

	output = '{}_trimal_{}.aln'.format(file_name, aut)
	os.system('/home/kika/programs/trimAl/source/trimal -in {} -out {} -{} -fasta'.format(file, output, aut))
	
	# output = '{}_trimal_{}.aln'.format(file_name, gt)
	# os.system('/home/kika/programs/trimAl/source/trimal -in {} -out {} -gt {} -fasta'.format(file, output, gt))
