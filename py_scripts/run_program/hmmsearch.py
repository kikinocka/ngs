#!/usr/bin/env python3
import os
import subprocess

os.chdir('/home/kika/ownCloud/blastocrithidia/ku_story/repair/missing_tryps/')
files = [x for x in os.listdir() if x.endswith('.hmm')]

db = '/home/kika/ownCloud/blastocrithidia/genome_assembly/jaculum_scaffolds_transc_translated.fasta'
orgn = 'jac'
threads = 4

for file in files:
	print(file)
	name = file.split('.')[0]
	out = orgn + '_' + name + '.hmm_search.out'
	subprocess.call('hmmsearch -o {} --cpu {} {} {}'.format(out, threads, file, db), 
		shell=True)
# --tblout {0}.table.txt 