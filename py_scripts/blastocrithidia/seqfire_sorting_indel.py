#!/usr/bin/env python3
import os
import subprocess

os.chdir('/home/kika/ownCloud/blastocrithidia/seqfire/simple_ins/')
files = sorted(os.listdir())

for file in files:
	print(file)
	name = file.split('_')[0]
	subprocess.call('grep -A40 "simple" {} > {}_simple.indel'.format(file, name), shell=True)
	subprocess.call('grep -A40 "complex" {} > {}_complex.indel'.format(file, name), shell=True)
