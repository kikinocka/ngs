#!/usr/bin/env python3
import os
import subprocess

os.chdir('/home/kika/ownCloud/pelomyxa/mito_proteins/import/tom-tim/hmm/')
files = [x for x in os.listdir() if x.endswith('.hmm')]
threads = 4
db = '/home/kika/ownCloud/pelomyxa/transcriptome_assembly/pelomyxa_trinity_translated.fasta'

for file in files:
	print(file)
	name = file.split('.')[0]
	orgn = 'pelo'
	out = orgn + '_' + name + '.hmm_search.out'
	subprocess.call('hmmsearch -o {} --cpu {} {} {}'.format(out, threads, file, db), 
		shell=True)
# --tblout {0}.table.txt 