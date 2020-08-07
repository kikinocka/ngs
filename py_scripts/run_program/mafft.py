#!/usr/bin/env python3
import os
import subprocess

mafft = '/Users/kika/miniconda3/bin/mafft'

os.chdir('/Users/kika/ownCloud/SAGs/mit/phylogenomics/ver5/')
files = [x for x in os.listdir() if x.endswith('.fa')]

for file in files:
	print(file)
	out = '{}.mafft.aln'.format(file.split('.fa')[0])
	subprocess.call('{} --thread 6 --maxiterate 100 --inputorder --auto {} > {}'.format(mafft, file, out), shell=True)

# #add to aligned sequences
# os.chdir('/Users/kika/ownCloud/membrane-trafficking/')
# existing = 'queries/SNAREs/R_SNARES_all.afa'
# new = 'trees/SNARE/R/ver3/euglenozoa.fa'
# out = 'trees/SNARE/R/ver3/r_v3.mafft.aln'
# subprocess.call('{} --add {} --thread 6 --inputorder {} > {}'.format(mafft, new, existing, out), shell=True)
