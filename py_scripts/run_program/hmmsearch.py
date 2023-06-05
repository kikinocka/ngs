#!/usr/bin/env python3
import os
import subprocess

hmmsearch = '/Users/kika/miniconda3/bin/hmmsearch'

os.chdir('/Users/kika/ownCloud/diplonema/pyruvate_metabolism/hydA/')
files = [x for x in os.listdir() if x.endswith('.hmm')]

db = '/Users/kika/ownCloud/diplonema/seq_data/diplonemids_transcriptomes/translations/1621_translated.fa'
orgn = '1621_trans'

for file in files:
	print(file)
	name = file.split('.hmm')[0]
	out = orgn + '_' + name + '.hmm_search.out'
	subprocess.call('{} -o {} --cpu 7 {} {}'.format(hmmsearch, out, file, db), shell=True)
# -o
# --tblout