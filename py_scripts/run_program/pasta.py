#!/usr/bin/python3
import os

pasta = '/home/nenarokova/tools/pasta_tools/pasta/run_pasta.py'

os.chdir('/media/4TB1/blastocrithidia/seqfire/dataset_sgOGs/')
files = sorted(os.listdir())

for file in files:
	if file.endswith('.fa'):
	# if '.aln' not in file:
		print(file)
		job_desc = file.split('.fa')[0]
		d = 'protein'
		os.system('{} -i {} -d {} -j {}'.format(pasta, file, d, job_desc))
