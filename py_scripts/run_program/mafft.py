#!/usr/bin/env python3
import os
import subprocess

mafft = '/Users/kika/miniconda3/bin/mafft'

# #align de-novo
# os.chdir('/Users/kika/ownCloud/Mic60-Mgm1-Opa1/coevolution-test/')
# files = [x for x in os.listdir() if x.endswith('subset.fa')]

# for file in files:
# 	print(file)
# 	out = '{}.mafft.aln'.format(file.split('.fa')[0])
# 	log = '{}.mafft.log'.format(file.split('.fa')[0])
# 	subprocess.call('{} --thread 7 --localpair --maxiterate 1000 --inputorder {} > {} 2> {}'.format(
# 		mafft, file, out, log), shell=True)

#add to aligned sequences
os.chdir('/Users/kika/ownCloud/anaeramoeba/trees/HOPS-CORVET/')
existing = 'HOPS_CORVET_T5.aln'
add = 'ver5/anaer.fa'
out = 'ver5/hops_corvet.mafft.aln'
log = 'ver5/hops_corvet.mafft.log'
subprocess.call('{} --add {} --thread 6 --inputorder {} > {} 2> {}'.format(mafft, add, existing, out, log), shell=True)
