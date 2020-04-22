#!/usr/bin/env python3
import os
import subprocess

hmmbuild = '/Users/kika/miniconda3/bin/hmmbuild'

os.chdir('/Users/kika/ownCloud/membrane-trafficking/queries/coats/hmm/COPII/')
files = os.listdir()
threads = 7

for file in files:
	if file.endswith('.aln'):
		print(file)
		name = file.split('.')[0]
		hmm = name + '.hmm_profile.hmm'
		summary = name + '.hmm_build.out'
		subprocess.call('{} -n {} -o {} --amino --cpu {} {} {}'.format(hmmbuild, name, summary, threads, hmm, file), 
			shell=True)
