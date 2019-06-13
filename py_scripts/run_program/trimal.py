#!/usr/bin/env python3
import os

os.chdir('/home/kika/MEGAsync/diplonema_paramylon/')
files = [x for x in os.listdir() if '.aln' in x]

for file in files:
	print(file)
	file_name = file.split('_')[0] + '_' + file.split('_')[1]
	option = 'automated1'
	output = '{}_trimal_{}.aln'.format(file_name, option)
	os.system('/home/kika/programs/trimAl/source/trimal -in {} -out {} -{} -fasta'.format(file, output, option))
	# os.system('/home/kika/programs/trimAl/source/trimal -in {} -out {} -gt {} -fasta'.format(file, output, option))
