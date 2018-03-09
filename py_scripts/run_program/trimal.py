#!/usr/bin/python3
import os

os.chdir('/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/sec/secA/')
files = os.listdir()

for file in files:
	if '.aln' in file:
		file_name = file.split('_mafft')[0]
		option = 'automated1'
		output = '{}_trimal_{}.aln'.format(file_name, option)
		os.system('/home/kika/programs/trimAl/source/trimal -in {} -out {} -{} -fasta'.format(file, output, option))