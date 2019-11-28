#!/usr/bin/env python3
import os
import subprocess

os.chdir('/home/kika/ownCloud/pelomyxa_schiedti/mito_proteins/pro_degradation/')
files = [x for x in os.listdir() if x.endswith('.fa')]
targetp='/home/kika/programs/targetp-1.1/targetp'


for file in files:
	print(file)
	out = file.split('.fa')[0] + '.targetp.txt'

	option = 'N'
	# option = 'P'
	
	subprocess.call('{} -{} -c {} > {}'.format(targetp, option, file, out), shell=True)
