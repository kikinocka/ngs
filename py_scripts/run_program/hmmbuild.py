#!/usr/bin/python3
import os
import subprocess

os.chdir('/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/TOC-TIC/')
files = os.listdir()
threads = 4

for file in files:
	if file.endswith('.fas'):
		print(file)
		name = file.split('_')[0]
		hmm = name + '_profile.hmm'
		summary = name + '_build.out'
		subprocess.call('hmmbuild -n {} -o {} --amino --cpu {} {} {}'.format(name, summary, threads, hmm, file), 
			shell=True)