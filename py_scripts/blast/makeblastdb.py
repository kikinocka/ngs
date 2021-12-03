#!/usr/bin/env python3
import os
import subprocess

os.chdir('/Users/kika/data/human/')
files = [x for x in os.listdir() if x.endswith('.faa')]
dbtype = 'prot'

for file in files: 
	print(file)
	fname = file.split('.faa')[0]
	subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(file, dbtype), shell=True)
