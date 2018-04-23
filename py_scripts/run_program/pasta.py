#!/usr/bin/python3
import os

os.chdir('/media/4TB1/blastocrithidia/api_NOG/apiNOG_raw_algs_single/')
files = sorted(os.listdir())
print(files)

for file in files:
	if file.endswith('.fa'):
	# if '.aln' not in file:
		print(file)
		job_desc = file.split('.')[1]
		d = 'protein'
		os.system('run_pasta.py -i {} -d {} -j {}'.format(file, d, job_desc))
