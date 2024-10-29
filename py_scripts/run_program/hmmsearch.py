#!/usr/bin/env python3
import os
import subprocess

hmmsearch = '/Users/kika/miniconda3/bin/hmmsearch'

os.chdir('/Users/kika/ownCloud/membrane-trafficking/diplonemids_ESCRTs/ESCRT-0/')
files = [x for x in os.listdir() if x.endswith('.hmm')]

db = '/Users/kika/data/fungi/GCF_000146045.2_R64_protein.faa'
orgn = 'scer_prot'
evalue = 1e-03

for file in files:
	print(file)
	name = file.split('.hmm')[0]
	out = orgn + '_' + name + '.hmmsearch.out'
	subprocess.call('{} -o {} --cpu 7 -E {} {} {}'.format(hmmsearch, out, evalue, file, db), shell=True)
# -o
# --tblout
