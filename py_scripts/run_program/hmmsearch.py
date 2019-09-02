#!/usr/bin/env python3
import os
import subprocess

os.chdir('/home/kika/MEGAsync/diplonema/nopaline_dehydrogenase/')
files = [x for x in os.listdir() if x.endswith('.hmm')]

db = '/home/kika/MEGAsync/Data/EG_RNAseq/EGALL_6frames.fasta'
orgn = 'eg'
threads = 4

for file in files:
	print(file)
	name = file.split('.')[0]
	out = orgn + '_' + name + '.hmm_search.out'
	subprocess.call('hmmsearch -o {} --cpu {} {} {}'.format(out, threads, file, db), 
		shell=True)
# --tblout {0}.table.txt 
