#!/usr/bin/env python3
import os
import subprocess

hmmsearch = '/Users/kika/miniconda3/bin/hmmsearch'

os.chdir('/Users/kika/ownCloud/membrane-trafficking/tom1/hmm/')
files = [x for x in os.listdir() if x.endswith('.hmm_profile')]

db = '/Users/kika/data/alveolates/chromera_velia_CDMZ01_translated.fa'
orgn = 'chromera'
threads = 6

for file in files:
	print(file)
	name = file.split('.hmm')[0]
	out = orgn + '_' + name + '.hmm_search.out'
	subprocess.call('{} -o {} --cpu {} {} {}'.format(hmmsearch, out, threads, file, db), shell=True)
#--tblout
