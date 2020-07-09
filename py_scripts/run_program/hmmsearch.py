#!/usr/bin/env python3
import os
import subprocess

hmmsearch = '/Users/kika/miniconda3/bin/hmmsearch'

os.chdir('/Users/kika/ownCloud/kinetoplastids/telomeres/Tb927.11.9870/')
files = [x for x in os.listdir() if x.endswith('.hmm_profile')]

db = '/Users/kika/ownCloud/data/kinetoplastids/genomes_fasta/Herpetomonas_muscarum_genome_translated.fa'
orgn = 'hmus'
threads = 3

for file in files:
	print(file)
	name = file.split('.hmm')[0]
	out = orgn + '_' + name + '.hmm_search.out'
	subprocess.call('{} -o {} --cpu {} {} {}'.format(hmmsearch, out, threads, file, db), shell=True)
# --tblout {0}.table.txt 
