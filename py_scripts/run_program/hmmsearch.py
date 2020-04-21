#!/usr/bin/env python3
import os
import subprocess

hmmsearch = '/Users/kika/miniconda3/bin/hmmsearch'

os.chdir('/Users/kika/ownCloud/membrane-trafficking/queries/coats/hmm/AP5/')
files = [x for x in os.listdir() if x.endswith('.hmm')]

db = '/Users/kika/ownCloud/data/kinetoplastids/TriTrypDB-46_LmajorFriedlin_Genome_translated.fa'
orgn = 'lmaj'
threads = 2

for file in files:
	print(file)
	name = file.split('.')[0]
	out = orgn + '_' + name + '.hmm_search.out'
	subprocess.call('{} -o {} --cpu {} {} {}'.format(hmmsearch, out, threads, file, db), shell=True)
# --tblout {0}.table.txt 
