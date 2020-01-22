#!/usr/bin/env python3
import os
import subprocess

targetp='/home/kika/programs/targetp-1.1/targetp'

os.chdir('/home/kika/MEGAsync/diplonema/catalase/targeting/')
files = [x for x in os.listdir() if x.endswith('apx.fa')]

for file in files:
	print(file)
	out = file.split('.fa')[0] + '.targetp.txt'

	# option = 'N'
	option = 'P'
	
	subprocess.call('{} -{} -c {} > {}'.format(targetp, option, file, out), shell=True)
