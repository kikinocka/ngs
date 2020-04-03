#!/usr/bin/env python3
import os
import subprocess

hmmsearch = '/home/osboxes/miniconda3/bin/hmmsearch'

os.chdir('/Dcko/ownCloud/membrane-trafficking/queries/coats/hmm/AP5/')
files = [x for x in os.listdir() if x.endswith('.hmm')]

db = '/Dcko/MEGAsync/Data/EL_RNAseq/el_merged_translated.fasta'
orgn = 'elon'
threads = 2

for file in files:
	print(file)
	name = file.split('.')[0]
	out = orgn + '_' + name + '.hmm_search.out'
	subprocess.call('{} -o {} --cpu {} {} {}'.format(hmmsearch, out, threads, file, db), shell=True)
# --tblout {0}.table.txt 
