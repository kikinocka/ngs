#!/usr/bin/env python3
import os
import subprocess

hmmsearch = '/Users/kika/miniconda3/bin/hmmsearch'

os.chdir('/Users/kika/ownCloud/membrane-trafficking/queries/HMMs/TRAPP-II/')
files = [x for x in os.listdir() if x.endswith('trs130_noeuglenozoa.hmm_profile')]

db = '/Users/kika/ownCloud/diplonema/seq_data/dpapillatum/representative_Ogar/dpap_transcripts_ed-minus_bac.transdecoder.fa'
orgn = 'dpap_tran'
evalue = 1e-03

for file in files:
	print(file)
	name = file.split('.hmm')[0]
	out = orgn + '_' + name + '.hmmsearch.out'
	subprocess.call('{} -o {} --cpu 7 -E {} {} {}'.format(hmmsearch, out, evalue, file, db), shell=True)
# -o
# --tblout
