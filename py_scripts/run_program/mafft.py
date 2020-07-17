#!/usr/bin/env python3
import os
import subprocess

mafft = '/Users/kika/miniconda3/bin/mafft'

# os.chdir('/Users/kika/ownCloud/SAGs/mit/nad11/ver2/')
# files = [x for x in os.listdir() if x.endswith('.fa')]

# for file in files:
# 	print(file)
# 	out = '{}.mafft.aln'.format(file.split('.fa')[0])
# 	subprocess.call('{} --thread 6 --maxiterate 100 --inputorder --auto {} > {}'.format(mafft, file, out), shell=True)

#add to aligned sequences
os.chdir('/Users/kika/ownCloud/membrane-trafficking/')
existing = 'queries/SNAREs/Qc_160302_2.afa'
new = 'trees/SNARE/Qc/ver9/euglenozoa.fa'
out = 'trees/SNARE/Qc/ver9/qc_v9.mafft.aln'
subprocess.call('{} --add {} --thread 6 --inputorder {} > {}'.format(mafft, new, existing, out), shell=True)
