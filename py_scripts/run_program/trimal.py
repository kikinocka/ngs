#!/usr/bin/python3
import os

os.chdir('/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Fd+FNR/Sulfite_reductase/cysJ/')
files = os.listdir()

for file in files:
	if '.aln' in file:
		print(file)
		file_name = file.split('.aln')[0]
		option = 'automated1'
		output = '{}_trimal_{}.aln'.format(file_name, option)
		os.system('/home/kika/programs/trimAl/source/trimal -in {} -out {} -{} -fasta'.format(file, output, option))
