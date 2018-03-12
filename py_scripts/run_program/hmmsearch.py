#!/usr/bin/python3
import os
import subprocess

os.chdir('/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/TOC-TIC/')
files = os.listdir()
threads = 4
db = '/home/kika/MEGAsync/Data/EL_RNAseq/20140707_ver._r2013-02-05/el_merged_translated.fasta'

for file in files:
	if file.endswith('.hmm'):
		print(file)
		name = file.split('_')[0]
		out = 'el_' + name + '_search.out'
		subprocess.call('hmmsearch -o {} --cpu {} {} {}'.format(out, threads, file, db), 
			shell=True)
