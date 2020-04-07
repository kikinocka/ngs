#!/usr/bin/env python3
import os
import subprocess

hmmsearch = '/home/osboxes/miniconda3/bin/hmmsearch'

os.chdir('/Dcko/ownCloud/membrane-trafficking/queries/coats/hmm/AP5/')
files = [x for x in os.listdir() if x.endswith('.hmm')]

db = '/Dcko/MEGAsync/Data/diplonemids_genomes/1621_spades_translated.fa'
orgn = '1621_gen'
threads = 2

for file in files:
	print(file)
	name = file.split('.')[0]
	out = orgn + '_' + name + '.hmm_search.out'
	subprocess.call('{} -o {} --cpu {} {} {}'.format(hmmsearch, out, threads, file, db), shell=True)
# --tblout {0}.table.txt 
