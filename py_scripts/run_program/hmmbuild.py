#!/usr/bin/env python3
import os
import subprocess

hmmbuild = '/Users/kika/miniconda3/bin/hmmbuild'

os.chdir('/Users/kika/ownCloud/kinetoplastids/angomonas/LOPIT-DC/EAPs/hmmsearch/rnd1/')
files = [x for x in os.listdir() if x.endswith('CAD2219389.mafft.aln')]
# files = [x for x in os.listdir() if x.startswith('hyp')]
threads = 7

for file in files:
	print(file)
	name = file.split('.mafft.aln')[0]
	hmm = name + '.hmm'
	summary = name + '.hmm.log'
	subprocess.call('{} -n {} -o {} --amino --cpu {} {} {}'.format(hmmbuild, name, summary, threads, hmm, file), 
		shell=True)
