#!/usr/bin/env python3
import os
import subprocess

hmmsearch = '/Users/kika/miniconda3/bin/hmmsearch'

os.chdir('/Users/kika/ownCloud/membrane-trafficking/queries/HMMs/RABs/')
files = [x for x in os.listdir() if x.endswith('B.hmm')]

db = '/Users/kika/ownCloud/diplonema/seq_data/diplonemids_transcriptomes/translations/1601_translated.fa'
orgn = '1601'
evalue = 1e-03

for file in files:
	print(file)
	name = file.split('.hmm')[0]
	out = orgn + '.' + name + '.hmmsearch.out'
	subprocess.call('{} -o {} --cpu 7 -E {} {} {}'.format(hmmsearch, out, evalue, file, db), shell=True)
# -o
# --tblout
