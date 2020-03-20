#!/usr/bin/env python3
import os
import subprocess

hmmbuild = '/home/osboxes/miniconda3/bin/hmmbuild'

os.chdir('/Dcko/ownCloud/membrane-trafficking/coat_queries/hmm/')
files = os.listdir()
threads = 2

for file in files:
	if file.endswith('.aln'):
		print(file)
		name = file.split('.')[0]
		hmm = name + '.hmm_profile.hmm'
		summary = name + '.hmm_build.out'
		subprocess.call('{} -n {} -o {} --amino --cpu {} {} {}'.format(hmmbuild, name, summary, threads, hmm, file), 
			shell=True)
