#!/usr/bin/env python3
import os
import subprocess

os.chdir('/Dcko/ownCloud/membrane-trafficking/coat_queries/hmm/')
files = os.listdir()
threads = 2

for file in files:
	if file.endswith('.aln'):
		print(file)
		name = file.split('_')[0]
		hmm = name + '_profile.hmm'
		summary = name + '_build.out'
		subprocess.call('hmmbuild -n {} -o {} --amino --cpu {} {} {}'.format(name, summary, threads, hmm, file), 
			shell=True)
