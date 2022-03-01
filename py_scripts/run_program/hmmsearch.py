#!/usr/bin/env python3
import os
import subprocess

hmmsearch = '/Users/kika/miniconda3/bin/hmmsearch'

os.chdir('/Users/kika/ownCloud/membrane-trafficking/queries/HMMs/Exocyst/')
files = [x for x in os.listdir() if x.endswith('.hmm_profile')]

db = '/Users/kika/ownCloud/diplonema/seq_data/dpapillatum/Gertraud/Dp_PB-MI_190104_dedup_cut_l100-submission-with-gene_models.faa'
orgn = 'dpap_prot'

for file in files:
	print(file)
	name = file.split('.hmm')[0]
	out = orgn + '_' + name + '.hmm_search.out'
	subprocess.call('{} -o {} --cpu 6 {} {}'.format(hmmsearch, out, file, db), shell=True)
# -o
# --tblout