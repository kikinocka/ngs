#!/usr/bin/env python3
import os
import subprocess

muscle = '/Users/kika/miniconda3/bin/muscle'

os.chdir('/Users/kika/ownCloud/kinetoplastids/base_J/trees/')
files = [x for x in os.listdir() if x.endswith('.fa')]
# files = [x for x in os.listdir() if x.startswith('CAD2221027.2')]

for file in files:
	print(file)
	out = '{}.muscle.aln'.format(file.split('.fa')[0])
	
	#short alns
	subprocess.call('{} -threads 5 -align {} -output {}'.format(muscle, file, out), shell=True)
	
	# #long alns
	# subprocess.call('{} -threads 5 -super5 {} -output {}'.format(muscle, file, out), shell=True)
