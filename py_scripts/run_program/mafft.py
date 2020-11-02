#!/usr/bin/env python3
import os
import subprocess

mafft = '/Users/kika/miniconda3/bin/mafft'

#align de-novo
os.chdir('/Users/kika/ownCloud/SAGs/ribosomal-import/alns/')
files = [x for x in os.listdir() if x.endswith('.fa')]

for file in files:
	print(file)
	out = '{}.mafft.aln'.format(file.split('.fa')[0])
	log = '{}.mafft.log'.format(file.split('.fa')[0])
	subprocess.call('{} --thread 7 --localpair --maxiterate 1000 --inputorder {} > {} 2> {}'.format(
		mafft, file, out, log), shell=True)

# #add to aligned sequences
# os.chdir('/Users/kika/ownCloud/membrane-trafficking/')
# existing = 'queries/ESCRTs/allSNF7.R3.trim.aln'
# new = 'trees/ESCRTs/snf7/ver2/euk_snf7.fa'
# out = 'trees/ESCRTs/snf7/ver2/snf7.mafft_add.aln'
# subprocess.call('{} --add {} --thread 6 --inputorder {} > {}'.format(mafft, new, existing, out), shell=True)
