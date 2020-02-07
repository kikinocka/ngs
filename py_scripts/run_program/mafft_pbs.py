#!/usr/bin/env python3
import os
import subprocess

files = [x for x in os.listdir() if x.endswith('.faa')]

for file in files:
	print(file)
	out = '{}.mafft.aln'.format(file.split('.faa')[0])
	subprocess.call('mafft --thread 20 --maxiterate 100 --inputorder --auto {} > {}'.format(file, out), 
		shell=True)
