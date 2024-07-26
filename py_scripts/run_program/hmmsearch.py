#!/usr/bin/env python3
import os
import subprocess

hmmsearch = '/Users/kika/miniconda3/bin/hmmsearch'

os.chdir('/Users/kika/ownCloud/membrane-trafficking/diplonemids_ESCRTs/Tb927.11.2020-2030/rnd2/')
files = [x for x in os.listdir() if x.endswith('2020.hmm')]

db = '/Users/kika/data/kinetoplastids/v68/Baya_translated.fa'
orgn = 'Baya'
evalue = 1e-03

for file in files:
	print(file)
	name = file.split('.hmm')[0]
	out = orgn + '_' + name + '.hmmsearch.out'
	subprocess.call('{} -o {} --cpu 7 -E {} {} {}'.format(hmmsearch, out, evalue, file, db), shell=True)
# -o
# --tblout
