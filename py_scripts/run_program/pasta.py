#!/usr/bin/python3
import os

os.chdir('/home/kika/MEGAsync/blasto_project/orthofinder/other_ogs/')
files = sorted(os.listdir())

for file in files:
	if file.endswith('_replaced2.fa'):
	# if '.aln' not in file:
		print(file)
		job_desc = file.split('_')[0]
		d = 'protein'
		os.system('run_pasta.py -i {} -d {} -j {}'.format(file, d, job_desc))
