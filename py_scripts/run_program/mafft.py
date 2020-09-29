#!/usr/bin/env python3
import os
import subprocess

mafft = '/Users/kika/miniconda3/bin/mafft'

# #align de-novo
# os.chdir('/Users/kika/ownCloud/membrane-trafficking/trees/ESCRTs/chmp7/')
# files = [x for x in os.listdir() if x.endswith('.fa')]

# for file in files:
# 	print(file)
# 	out = '{}.mafft.aln'.format(file.split('.fa')[0])
# 	subprocess.call('{} --thread 6 --maxiterate 100 --inputorder --auto {} > {}'.format(mafft, file, out), shell=True)

#add to aligned sequences
os.chdir('/Users/kika/ownCloud/membrane-trafficking/')
existing = 'queries/ESCRTs/allSNF7.R3.trim.aln'
new = 'trees/ESCRTs/chmp7/ver4/snf7.fa'
out = 'trees/ESCRTs/chmp7/ver4/chmp7.mafft_add.aln'
subprocess.call('{} --add {} --thread 6 --inputorder {} > {}'.format(mafft, new, existing, out), shell=True)
