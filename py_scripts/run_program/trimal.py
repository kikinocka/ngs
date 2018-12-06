#!/usr/bin/env python3
import os

os.chdir('/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Fd+FNR/chlamydial/')
files = os.listdir()

for file in files:
	if 'MAFFT' in file:
		print(file)
		file_name = file.split('_')[0]
		option = 'gt 0.5'
		output = '{}_trimal_0.5.aln'.format(file_name)
		os.system('/home/kika/programs/trimAl/source/trimal -in {} -out {} -{} -fasta'.format(file, output, option))
