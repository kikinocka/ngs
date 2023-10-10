#!/usr/bin/env python3
import os
import subprocess

hmmsearch = '/Users/kika/miniconda3/bin/hmmsearch'

os.chdir('/Users/kika/ownCloud/membrane-trafficking/diplonemids_ESCRTs/HMM/')
files = [x for x in os.listdir() if x.endswith('.hmm')]

db = '/Users/kika/data/eukprot_v3/EP01052_Picozoa_sp_SAG31.fasta'
orgn = 'EP01052_Picozoa_sp_SAG31'

for file in files:
	print(file)
	name = file.split('.hmm')[0]
	out = orgn + '_' + name + '.hmmsearch.out'
	subprocess.call('{} -o {} --cpu 7 {} {}'.format(hmmsearch, out, file, db), shell=True)
# -o
# --tblout
