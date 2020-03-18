#!/usr/bin/env python3
import os
import subprocess

os.chdir('/Dcko/ownCloud/membrane-trafficking/coat_queries/hmm/')
files = [x for x in os.listdir() if x.endswith('.hmm')]

db = '/Dcko/MEGAsync/Data/dpapilatum/dpap_genome_translated.fa'
orgn = 'dpap_gen'
threads = 2

for file in files:
	print(file)
	name = file.split('.')[0]
	out = orgn + '_' + name + '.hmm_search.out'
	subprocess.call('hmmsearch -o {} --cpu {} {} {}'.format(out, threads, file, db), shell=True)
# --tblout {0}.table.txt 
