#!/usr/bin/env python3
import os
import subprocess

hmmsearch = '/Users/kika/miniconda3/bin/hmmsearch'

os.chdir('/Users/kika/ownCloud/Mic60-Mgm1-Opa1/hsp70/')
files = [x for x in os.listdir() if x.endswith('.hmm_profile')]

db = '/Users/kika/data/eukprot/eukprot_v2_proteins_renamed.faa'
orgn = 'eukprot'
threads = 6

for file in files:
	print(file)
	name = file.split('.hmm')[0]
	out = orgn + '_' + name + '.hmm_search.table'
	subprocess.call('{} --tblout {} --cpu {} {} {}'.format(hmmsearch, out, threads, file, db), shell=True)
# -o
# --tblout