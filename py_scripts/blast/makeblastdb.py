#!/usr/bin/env python3
import os
import subprocess

os.chdir('/Users/kika/data/eukprot/')
files = [x for x in os.listdir() if x.endswith('.fasta')]
dbtype = 'nucl'

for file in files: 
	print(file)
	fname = file.split('.fasta')[0]
	subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(file, dbtype), shell=True)
