#!/usr/bin/env python3
import os
import subprocess

os.chdir('/Dcko/ownCloud/proteromonas/peroxisome/3-hydroxacyl-CoA_dehydrogenase/')
files = [x for x in os.listdir() if x.endswith('.hmm')]

db = '/Dcko/MEGAsync/Data/stramenopiles/Proteromonas_l_genomic_translated.fa'
orgn = 'prot'
threads = 2

for file in files:
	print(file)
	name = file.split('.')[0]
	out = orgn + '_' + name + '.hmm_search.out'
	subprocess.call('hmmsearch -o {} --cpu {} {} {}'.format(out, threads, file, db), shell=True)
# --tblout {0}.table.txt 
