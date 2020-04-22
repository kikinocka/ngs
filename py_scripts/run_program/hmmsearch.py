#!/usr/bin/env python3
import os
import subprocess

hmmsearch = '/Users/kika/miniconda3/bin/hmmsearch'

os.chdir('/Users/kika/ownCloud/membrane-trafficking/queries/coats/hmm/COPII/')
files = [x for x in os.listdir() if x.endswith('.hmm')]

db = '/Users/kika/ownCloud/data/diplonemids_genomes/1610_spades_translated.fa'
orgn = 'amot'
threads = 7

for file in files:
	print(file)
	name = file.split('.')[0]
	out = orgn + '_' + name + '.hmm_search.out'
	subprocess.call('{} -o {} --cpu {} {} {}'.format(hmmsearch, out, threads, file, db), shell=True)
# --tblout {0}.table.txt 
