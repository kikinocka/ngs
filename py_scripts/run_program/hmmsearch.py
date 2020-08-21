#!/usr/bin/env python3
import os
import subprocess

hmmsearch = '/Users/kika/miniconda3/bin/hmmsearch'

os.chdir('/Users/kika/ownCloud/membrane-trafficking/queries/HMMs/')
files = [x for x in os.listdir() if x.endswith('.hmm_profile')]

db = '/Users/kika/ownCloud/data/diplonemids_genomes/1621_spades_translated.fa'
orgn = 'nkar'
threads = 6

for file in files:
	print(file)
	name = file.split('.hmm')[0]
	out = orgn + '_' + name + '.hmm_search.out'
	subprocess.call('{} -o {} --cpu {} {} {}'.format(hmmsearch, out, threads, file, db), shell=True)
#--tblout
