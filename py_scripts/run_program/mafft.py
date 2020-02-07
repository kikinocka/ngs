#!/usr/bin/env python3
import os
import subprocess

os.chdir('/Dcko/ownCloud/SAGs/phylogenomics/Bordor-alignments_euglenids-July2019/euglenozoa/')
files = [x for x in os.listdir() if x.endswith('.faa')]

for file in files:
	print(file)
	out = '{}.mafft.aln'.format(file.split('.faa')[0])
	subprocess.call('mafft --thread 4 --inputorder --auto {} > {}'.format(file, out), 
		shell=True)
