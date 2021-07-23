#!/usr/bin/env python3
import os
import subprocess

mafft = '/Users/kika/miniconda3/bin/mafft'

#align de-novo
os.chdir('/Users/kika/ownCloud/membrane-trafficking/trees/RABs/rab32')
files = [x for x in os.listdir() if x.endswith('.fa')]

for file in files:
	print(file)
	out = '{}.mafft.aln'.format(file.split('.fa')[0])
	log = '{}.mafft.log'.format(file.split('.fa')[0])
	subprocess.call('{} --thread 7 --localpair --maxiterate 1000 --inputorder {} > {} 2> {}'.format(
		mafft, file, out, log), shell=True)

# #add to aligned sequences
# os.chdir('/Users/kika/ownCloud/membrane-trafficking/trees/ESCRTs/chmp7-NT_vps25/')
# existing = 'Shweta_alns/SNF8_R1.aln'
# add = 'diplo.fa'
# out = 'chmp7-NT_vps25.mafft.aln'
# log = 'chmp7-NT_vps25.mafft.log'
# subprocess.call('{} --add {} --thread 7 --inputorder {} > {} 2> {}'.format(mafft, add, existing, out, log), shell=True)
# # subprocess.call('{} --addfragments {} --thread 7 --inputorder {} > {} 2> {}'.format(mafft, add, existing, out, log), shell=True)
