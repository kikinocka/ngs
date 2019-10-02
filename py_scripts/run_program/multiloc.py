#!/usr/bin/env python2
import os
import subprocess

multiloc = '/home/kika/tools/MultiLoc2/src/multiloc2_prediction.py'

os.chdir('/home/kika/pelomyxa_schiedti/predicted_proteins/')
files = [x for x in os.listdir() if x.endswith('.fa')]

for file in files:
	print(file)
	out = file.split('.fa')[0] + '.multiloc.txt'

	option = 'animal'
	# option = 'fungal'
	# option = 'plant'
	
	subprocess.call('python2 {} -fasta={} -origin={} -predictor=LowRes -result={} -output=simple'.format(
		multiloc, file, option, out), shell=True)
