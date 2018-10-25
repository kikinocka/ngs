#!/usr/bin/env python
import os
import subprocess

seqfire='/home/kika/programs/seqFIRE/seqfire.py'

os.chdir('/home/kika/ownCloud/blastocrithidia/orthofinder/sg_ogs/jac_renamed/seqfire/')
files = sorted(os.listdir())

for file in files:
	if file.endswith('.aln'):
		subprocess.call('python2 {} -i {} -a 1 -b 1 -p False'.format(seqfire, file), shell=True)
		print(file)
