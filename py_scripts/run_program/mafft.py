#!/usr/bin/env python3
import os
import subprocess

mafft = '/Users/kika/miniconda3/bin/mafft'

os.chdir('/Users/kika/ownCloud/SAGs/phylogenomics/ver8_GL/')
files = [x for x in os.listdir() if x.endswith('.fa')]

for file in files:
	print(file)
	out = '{}.mafft.aln'.format(file.split('.fa')[0])
	subprocess.call('{} --thread 7 --maxiterate 100 --inputorder --auto {} > {}'.format(mafft, file, out), shell=True)

# #add to aligned sequences
# os.chdir('/Users/kika/ownCloud/membrane-trafficking/')
# existing = 'queries/SNAREs/S17.Qa.6.afa'
# new = 'trees/SNARE/Qa/ver6/euglenozoa.fa'
# out = 'trees/SNARE/Qa/ver6/qa.mafft.aln'
# subprocess.call('{} --add {} --thread 7 --inputorder {} > {}'.format(mafft, new, existing, out), shell=True)
