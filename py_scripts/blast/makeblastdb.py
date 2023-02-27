#!/usr/bin/env python3
import os
import subprocess

os.chdir('/Users/kika/data/kinetoplastids/')
files = [x for x in os.listdir() if x.endswith('Spodlipaevi_CER4_sorted_renamed.masked.fasta')]
dbtype = 'nucl'

for file in files: 
	print(file)
	fname = file.split('.fa')[0]
	subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(file, dbtype), shell=True)
