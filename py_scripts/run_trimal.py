#!/usr/bin/python3
import os

os.chdir('/home/kika/MEGAsync/blasto_project/genes/tRNAs/iqtree/')
files = os.listdir()

for file in files:
	if '.aln' in file:
		file_name = file.split('_pasta')[0]
		option = 'gappyout'
		output = '{}_trimal_{}.fasta'.format(file_name, option)
		os.system('/home/kika/programs/trimAl/source/trimal -in {} -out {} -{} -fasta'.format(file, output, option))