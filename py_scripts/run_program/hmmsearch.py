#!/usr/bin/env python3
import os
import subprocess

hmmsearch = '/Users/kika/miniconda3/bin/hmmsearch'

os.chdir('/Users/kika/ownCloud/quinones/coq_profiles/')
files = [x for x in os.listdir() if x.endswith('COQ6.hmm')]

db = '/Users/kika/ownCloud/diplonema/seq_data/diplonemids_transcriptomes/translations/1621_translated.fa'
orgn = '1621'
evalue = 1e-05

for file in files:
	print(file)
	name = file.split('.hmm')[0]
	out = orgn + '.' + name + '.hmmsearch.out'
	subprocess.call('{} -o {} --cpu 7 -E {} {} {}'.format(hmmsearch, out, evalue, file, db), shell=True)
# -o
# --tblout
