#!/usr/bin/python2
import os
import subprocess

seqfire='/home/kika/tools/seqfire.py'

os.chdir('/media/4TB1/blastocrithidia/seqfire/alignments_sgOGs/')
files = sorted(os.listdir('/media/4TB1/blastocrithidia/seqfire/alignments_sgOGs/'))

for file in files:
	if file.endswith('.aln'):
		print(file)
		subprocess.call('python2 {} -i {} -a 1 -b 1 -p True'.format(seqfire, file), shell=True)
