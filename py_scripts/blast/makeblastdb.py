#!/usr/bin/env python3
import os
import subprocess

os.chdir('/Users/kika/ownCloud/diplonema/seq_data/dpapillatum/Gertraud/')
files = [x for x in os.listdir() if x.endswith('Dp_PB-MI_190104_dedup_cut_l100-submission-with-gene_models.faa')]
dbtype = 'prot'

for file in files: 
	print(file)
	fname = file.split('.faa')[0]
	subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(file, dbtype), shell=True)
