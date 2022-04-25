#!/usr/bin/env python3
import os
import subprocess

hmmsearch = '/Users/kika/miniconda3/bin/hmmsearch'

os.chdir('/Users/kika/ownCloud/blastocrithidia/genes/NMD/ciliates/')
files = [x for x in os.listdir() if x.endswith('.hmm_profile')]

db = '/Users/kika/data/eukprot/EP00360_Condylostoma_magnum.fasta'
orgn = 'EP00360'

for file in files:
	print(file)
	name = file.split('.hmm')[0]
	out = orgn + '_' + name + '.hmm_search.table'
	subprocess.call('{} --tblout {} --cpu 7 {} {}'.format(hmmsearch, out, file, db), shell=True)
# -o
# --tblout