#!/usr/bin/python3
import os

os.chdir('/home/kika/MEGAsync/blasto_project/orthofinder/sc_ogs/problems/new/')
files = os.listdir()

for file in files:
	if '.fa' in file:
	# if '.aln' not in file:
		print(file)
		job_desc = file.split('_replaced2.fa')[0]
		d = 'protein'
		os.system('run_pasta.py -i {} -d {} -j {}'.format(file, d, job_desc))