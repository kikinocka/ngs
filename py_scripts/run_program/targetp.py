#!/usr/bin/env python3
import os
import subprocess

targetp='/home/osboxes/programs/targetp-2.0/bin/targetp'

os.chdir('/Dcko/MEGAsync/diplonema/catalase/targeting/')
files = [x for x in os.listdir() if x.endswith('missing.fa')]

for file in files:
	print(file)
	out = file.split('.fa')[0] + '.targetp.txt'

	# #TargetP-1.1
	# option = 'N'
	# option = 'P'
	# subprocess.call('{} -{} -c {} > {}'.format(targetp, option, file, out), shell=True)

	#TagetP-2
	option = 'non-pl'
	# option = 'pl'
	subprocess.call('{} -fasta {} -org {} -format short'.format(targetp, file, option), shell=True)
