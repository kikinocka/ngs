#!/usr/bin/env python3
import os

os.chdir('/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Glycerolipids/SQD_pathway/SQD2_tree/')
files = os.listdir()

for file in files:
	if 'MAFFT' in file:
		print(file)
		file_name = file.split('_')[0]
		option = 'automated1'
		output = '{}_trimal_{}.aln'.format(file_name, option)
		os.system('/home/kika/programs/trimAl/source/trimal -in {} -out {} -{} -fasta'.format(file, output, option))
