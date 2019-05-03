#!/usr/bin/env python3
import os
import subprocess

os.chdir('/home/kika/MEGAsync/diplonema_mt/dpap/')
files = os.listdir()
threads = 4

for file in files:
	if file.endswith('.txt'):
		print(file)
		name = file.split('_')[0]
		hmm = name + '_profile.hmm'
		summary = name + '_build.out'
		subprocess.call('hmmbuild -n {} -o {} --amino --cpu {} {} {}'.format(name, summary, threads, hmm, file), 
			shell=True)