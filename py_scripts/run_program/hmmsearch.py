#!/usr/bin/env python3
import os
import subprocess

hmmsearch = '/Users/kika/miniconda3/bin/hmmsearch'

os.chdir('/Users/kika/ownCloud/membrane-trafficking/queries/HMMs/MTCs/')
files = [x for x in os.listdir() if x.endswith('sec39.hmm_profile')]

db = '/Users/kika/data/kinetoplastids/TriTrypDB-54_BsaltansLakeKonstanz_AnnotatedProteins.fasta'
orgn = 'bsal_prot'

for file in files:
	print(file)
	name = file.split('.hmm')[0]
	out = orgn + '_' + name + '.hmm_search.out'
	subprocess.call('{} -o {} --cpu 6 {} {}'.format(hmmsearch, out, file, db), shell=True)
# -o
# --tblout