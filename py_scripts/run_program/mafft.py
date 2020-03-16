#!/usr/bin/env python3
import os
import subprocess

# mafft = '/home/osboxes/miniconda3/bin/mafft'

os.chdir('/Dcko/MEGAsync/Euglena_longa/2013_Sekvenovanie/Tetrapyrroles/tRNA-Glu/')
files = [x for x in os.listdir() if x.endswith('.fa')]

for file in files:
	print(file)
	out = '{}.mafft.aln'.format(file.split('.fa')[0])
	subprocess.call('mafft --thread 2 --maxiterate 100 --inputorder --auto {} > {}'.format(file, out), shell=True)
	# subprocess.call('{} --thread 2 --maxiterate 100 --inputorder --auto {} > {}'.format(mafft, file, out), shell=True)
