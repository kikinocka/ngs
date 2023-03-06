#!/usr/bin/env python3
import os
import subprocess

os.chdir('/Users/kika/ownCloud/blasto_comparative/genomes/')
files = [x for x in os.listdir() if x.endswith('Braa_genome_final_corrected2_masked.fa')]
dbtype = 'nucl'

for file in files: 
	print(file)
	fname = file.split('.fa')[0]
	subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(file, dbtype), shell=True)
