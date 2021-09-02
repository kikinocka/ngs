#!/usr/bin/env python3
import os
import subprocess

hmmscan = '/Users/kika/miniconda3/bin/hmmscan'

os.chdir('/Users/kika/ownCloud/membrane-trafficking/trees/ARFs/unclassified/')
files = [x for x in os.listdir() if x.endswith('.fa')]

db = '/Users/kika/ownCloud/ARF_db-hmmscan/ScrollSaw_all.hmm'

for file in files:
	print(file)
	name = file.split('.fa')[0]
	out = name + '.hmmscan.table'
	subprocess.call('{} --tblout {} --cpu 6 {} {}'.format(hmmscan, out, db, file), shell=True)
# -o
# --tblout
