#!/usr/bin/env python3
import os
import subprocess

os.chdir('/Users/kika/data/amoebozoa/')
files = [x for x in os.listdir() if x.endswith('fasta')]
dbtype = 'prot'

for file in files: 
	print(file)
	# fname = file.split('.faa')[0]
	subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(file, dbtype), shell=True)
