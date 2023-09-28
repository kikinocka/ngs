#!/usr/bin/env python3
import os
import subprocess

muscle = '/Users/kika/miniconda3/bin/muscle'

#align de-novo
os.chdir('/Users/kika/ownCloud/blasto_comparative/orthofinder_Aug18/blasto-specific/OGs_fasta/')
files = [x for x in os.listdir() if x.endswith('.fa')]

for file in files:
	print(file)
	out = '{}.muscle.aln'.format(file.split('.fa')[0])
	log = '{}.muscle.log'.format(file.split('.fa')[0])
	subprocess.call('{} -super5 {} -output {} -threads 6 2> {}'.format(muscle, file, out, log), shell=True)
