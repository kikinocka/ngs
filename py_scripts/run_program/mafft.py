#!/usr/bin/env python3
import os
import subprocess

mafft = '/Users/kika/miniconda3/bin/mafft'

# os.chdir('/Users/kika/ownCloud/SAGs/phylogenomics/ver7_GL/dataset/')
# files = [x for x in os.listdir() if x.endswith('.fa')]

# for file in files:
# 	print(file)
# 	out = '{}.mafft.aln'.format(file.split('.fa')[0])
# 	subprocess.call('{} --thread 7 --maxiterate 100 --inputorder --auto {} > {}'.format(mafft, file, out), shell=True)
# 	subprocess.call('{} --thread 2 --maxiterate 100 --inputorder --auto {} > {}'.format(mafft, file, out), shell=True)

os.chdir('/Users/kika/ownCloud/membrane-trafficking/')
existing = 'queries/SNAREs/Qc_160302_2.afa'
new = 'trees/SNARE/Qc/ver7/euglenozoa.fa'
out = 'trees/SNARE/Qc/ver7/qc.mafft.aln'
subprocess.call('{} --add {} --thread 7 --inputorder {} > {}'.format(mafft, new, existing, out), shell=True)
