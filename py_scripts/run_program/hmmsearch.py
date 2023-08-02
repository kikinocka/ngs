#!/usr/bin/env python3
import os
import subprocess

hmmsearch = '/Users/kika/miniconda3/bin/hmmsearch'

os.chdir('/Users/kika/ownCloud/blastocrithidia/genes/amastins/')
files = [x for x in os.listdir() if x.endswith('.hmm')]

db = '/Users/kika/ownCloud/blastocrithidia/genome_assembly/p57_polished_translated.fa'
orgn = 'bnon_gen'

for file in files:
	print(file)
	name = file.split('.hmm')[0]
	out = orgn + '_' + name + '.hmmsearch.out'
	subprocess.call('{} -o {} --cpu 7 {} {}'.format(hmmsearch, out, file, db), shell=True)
# -o
# --tblout