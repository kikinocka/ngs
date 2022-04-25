#!/usr/bin/env python3
import os
import subprocess

hmmbuild = '/Users/kika/miniconda3/bin/hmmbuild'

os.chdir('/Users/kika/ownCloud/blastocrithidia/genes/NMD/ciliates/')
files = [x for x in os.listdir() if x.endswith('upf3.mafft.aln')]
threads = 7

for file in files:
	print(file)
	name = file.split('.mafft')[0]
	hmm = name + '.hmm_profile'
	summary = name + '.hmm_build'
	subprocess.call('{} -n {} -o {} --amino --cpu {} {} {}'.format(hmmbuild, name, summary, threads, hmm, file), 
		shell=True)
