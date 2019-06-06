#!/usr/bin/env python3
import os
import subprocess

os.chdir('/home/kika/ownCloud/euglenophytes/trees/')
files = [x for x in os.listdir() if x.endswith('.fas')]

for file in files:
	print(file)
	out = '{}_MAFFT.aln'.format(file.split('.fa')[0])
	subprocess.call('mafft --thread 4 --threadit 0 --inputorder --auto {} > {}'.format(file, out), 
		shell=True)
