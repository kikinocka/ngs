#!/usr/bin/env python3
import os
import subprocess

os.chdir('/Dcko/ownCloud/proteromonas/PXMP2_tree/')
files = [x for x in os.listdir() if x.endswith('2.fa')]

for file in files:
	print(file)
	out = '{}.mafft.aln'.format(file.split('.faa')[0])
	subprocess.call('mafft --thread 2 --maxiterate 100 --inputorder --auto {} > {}'.format(file, out), shell=True)
