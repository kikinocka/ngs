#!/usr/bin/env python3
import os
import subprocess

hmmsearch = '/Users/kika/miniconda3/bin/hmmsearch'

os.chdir('/Users/kika/ownCloud/membrane-trafficking/queries/HMMs/GARP/')
files = [x for x in os.listdir() if x.endswith('.hmm_profile')]

db = '/Users/kika/ownCloud/Eutreptiella/NIES_MMETSP0039_clean.pep.fa.txt'
orgn = 'eut'

for file in files:
	print(file)
	name = file.split('.hmm')[0]
	out = orgn + '_' + name + '.hmm_search.out'
	subprocess.call('{} -o {} --cpu 6 {} {}'.format(hmmsearch, out, file, db), shell=True)
# -o
# --tblout