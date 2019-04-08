#!/usr/bin/python3
import os

# pasta = '/home/nenarokova/tools/pasta_tools/pasta/run_pasta.py'

os.chdir('/home/kika/ownCloud/pelomyxa/mito_proteins/fes_cluster_assembly/nif/nifU_tree/')
files = [x for x in sorted(os.listdir()) if x.endswith('deduplicated.fa')]

for file in files:
	print(file)
	job_desc = file.split('.fa')[0]
	d = 'protein'
	os.system('run_pasta.py -i {} -d {} -j {}'.format(file, d, job_desc))
