#!/usr/bin/env python3
import os
import subprocess

os.chdir('/home/kika/pelomyxa_schiedti/predicted_proteins_transdecoder/')
files = [x for x in os.listdir() if x.endswith('_renamed.fa')]

for file in files:
	print(file)
	out = file.split('.fa')[0] + '.targetp.txt'

	option = 'N'
	# option = 'P'
	
	subprocess.call('targetp -{} -c {} > {}'.format(option, file, out), shell=True)
