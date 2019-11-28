#!/usr/bin/env python3
import os
import subprocess

os.chdir('/home/kika/ownCloud/pelomyxa_schiedti/mito_proteins/fes_cluster_assembly/nif/nifS_tree/ver2/')
files = [x for x in os.listdir() if x.endswith('.fa')]

for file in files:
	print(file)
	out = '{}_mafft.aln'.format(file.split('.fa')[0])
	subprocess.call('mafft --thread 4 --inputorder --auto {} > {}'.format(file, out), 
		shell=True)
