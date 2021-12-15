#!/usr/bin/env python3
import os
import subprocess

hmmbuild = '/Users/kika/miniconda3/bin/hmmbuild'

os.chdir('/Users/kika/ownCloud/membrane-trafficking/queries/HMMs/')
files = os.listdir()
threads = 7

for file in files:
	if file.endswith('.aln'):
		print(file)
		name = file.split('.mafft')[0]
		hmm = name + '.hmm_profile'
		summary = name + '.hmm_build'
		subprocess.call('{} -n {} -o {} --amino --cpu {} {} {}'.format(hmmbuild, name, summary, threads, hmm, file), 
			shell=True)
