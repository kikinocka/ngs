#!/usr/bin/env python3
import os
import subprocess

mafft = '/home/osboxes/miniconda3/bin/mafft'

os.chdir('/Dcko/ownCloud/membrane-trafficking/queries/coats/hmm/AP4/')
files = [x for x in os.listdir() if x.endswith('.fa')]

for file in files:
	print(file)
	out = '{}.mafft.aln'.format(file.split('.fa')[0])
	subprocess.call('{} --thread 2 --maxiterate 100 --inputorder --auto {} > {}'.format(mafft, file, out), shell=True)
	# subprocess.call('{} --thread 2 --maxiterate 100 --inputorder --auto {} > {}'.format(mafft, file, out), shell=True)
