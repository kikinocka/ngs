#!/usr/bin/env python3
import os
import subprocess

hmmsearch = '/Users/kika/miniconda3/bin/hmmsearch'

os.chdir('/Users/kika/ownCloud/membrane-trafficking/queries/HMMs/SNAREs/')
files = [x for x in os.listdir() if x.endswith('qa1.hmm_profile')]

db = '/Users/kika/ownCloud/Euglena_longa/EL_RNAseq/el_merged_translated.fasta'
orgn = 'elon'
evalue = 1e-03

for file in files:
	print(file)
	name = file.split('.hmm')[0]
	out = orgn + '_' + name + '.hmmsearch.out'
	subprocess.call('{} -o {} --cpu 7 -E {} {} {}'.format(hmmsearch, out, evalue, file, db), shell=True)
# -o
# --tblout
