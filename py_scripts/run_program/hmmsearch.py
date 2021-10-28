#!/usr/bin/env python3
import os
import subprocess

hmmsearch = '/Users/kika/miniconda3/bin/hmmsearch'

os.chdir('/Users/kika/ownCloud/archamoebae/import/hmms/')
files = [x for x in os.listdir() if x.endswith('.hmm')]

db = '/Users/kika/ownCloud/archamoebae/entamoeba_histolytica/AmoebaDB-53_EhistolyticaHM1IMSS_AnnotatedProteins.fasta'
orgn = 'ehis'

for file in files:
	print(file)
	name = file.split('.hmm')[0]
	out = orgn + '_' + name + '.hmm_search.table'
	subprocess.call('{} --tblout {} --cpu 6 {} {}'.format(hmmsearch, out, file, db), shell=True)
# -o
# --tblout