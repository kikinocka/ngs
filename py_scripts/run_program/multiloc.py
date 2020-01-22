#!/usr/bin/env python3
import os
import subprocess

multiloc = '/home/kika/programs/MultiLoc2-26-10-2009/src/multiloc2_prediction.py'

os.chdir('/home/kika/MEGAsync/diplonema/catalase/targeting/')
files = [x for x in os.listdir() if x.endswith('apx.fa')]

for file in files:
	print(file)
	name = file.split('.fa')[0]
	
	# option = 'animal'
	# option = 'fungal'
	option = 'plant'
	
	out = '{}.multiloc_{}.tsv'.format(name, option)
	subprocess.call('python2 {} -fasta={} -origin={} -predictor=LowRes -result={} -output=simple'.format(
		multiloc, file, option, out), shell=True)
