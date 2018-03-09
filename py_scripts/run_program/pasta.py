#!/usr/bin/python3
import os

os.chdir('/home/kika/MEGAsync/blasto_project/genes/catalase/nt/')
files = os.listdir()

for file in files:
	if file.endswith('.fas'):
	# if '.aln' not in file:
		print(file)
		job_desc = file.split('_replaced.fa')[0]
		d = 'DNA'
		os.system('run_pasta.py -i {} -d {} -j {}'.format(file, d, job_desc))