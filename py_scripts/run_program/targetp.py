#!/usr/bin/env python3
import os
import subprocess

targetp='/Users/kika/programs/targetp-2.0/bin/targetp'

os.chdir('/Users/kika/ownCloud/diplonema/cardiolipin/CLS_pld/')
files = [x for x in os.listdir() if x.endswith('diplonemy_cls.fasta')]

for file in files:
	print(file)

	# #TargetP-1.1
	# option = 'N'
	# option = 'P'
	# out = file.split('.fa')[0] + '.targetp.txt'
	# subprocess.call('{} -{} -c {} > {}'.format(targetp, option, file, out), shell=True)

	#TagetP-2
	option = 'non-pl'
	# option = 'pl'
	subprocess.call('{} -fasta {} -org {} -format short'.format(targetp, file, option), shell=True)
