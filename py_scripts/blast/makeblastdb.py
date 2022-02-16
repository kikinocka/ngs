#!/usr/bin/env python3
import os
import subprocess

os.chdir('/Users/kika/data/eukprot/')
files = [x for x in os.listdir() if x.endswith('EP00441_Pelagodinium_beii.fasta')]
dbtype = 'prot'

for file in files: 
	print(file)
	fname = file.split('.faa')[0]
	subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(file, dbtype), shell=True)
