#!/usr/bin/env python3
import os
import subprocess

hmmsearch = '/Users/kika/miniconda3/bin/hmmsearch'

os.chdir('/Users/kika/ownCloud/archamoebae/rho/HMM/')
files = [x for x in os.listdir() if x.endswith('.hmm_profile')]

db = '/Users/kika/ownCloud/archamoebae/entamoeba_histolytica/AmoebaDB-53_EhistolyticaHM1IMSS_AnnotatedProteins.fasta'
orgn = 'ehis_prot'

for file in files:
	print(file)
	name = file.split('.hmm')[0]
	out = orgn + '_' + name + '.hmm_search.txt'
	subprocess.call('{} -o {} --cpu 7 {} {}'.format(hmmsearch, out, file, db), shell=True)
# -o
# --tblout