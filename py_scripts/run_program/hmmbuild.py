#!/usr/bin/env python3
import os
import subprocess

hmmbuild = '/Users/kika/miniconda3/bin/hmmbuild'

os.chdir('/Users/kika/ownCloud/euglenozoa_mito/ERMES/')
files = [x for x in os.listdir() if x.endswith('.aln')]
# files = [x for x in os.listdir() if x.startswith('hyp')]
threads = 7

for file in files:
	print(file)
	name = file.split('.aln')[0]
	hmm = name + '.hmm'
	summary = name + '.hmmbuild.log'
	subprocess.call('{} -n {} -o {} --amino --cpu {} {} {}'.format(hmmbuild, name, summary, threads, hmm, file), 
		shell=True)
