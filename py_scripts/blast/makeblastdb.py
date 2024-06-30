#!/usr/bin/env python3
import os
import subprocess

os.chdir('/Users/kika/ownCloud/Euglena_gracilis/RNA-Seq/')
files = [x for x in os.listdir() if x.endswith('GEFR01.1.fsa_nt')]
dbtype = 'nucl'

for file in files: 
	print(file)
	# fname = file.split('.faa')[0]
	subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(file, dbtype), shell=True)
