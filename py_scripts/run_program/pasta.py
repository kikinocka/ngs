#!/usr/bin/python3
import os

os.chdir('/home/kika/MEGAsync/blasto_project/genes/known_secondary_structures/PASTA/')
files = sorted(os.listdir())

for file in files:
	if file.endswith('.fa'):
	# if '.aln' not in file:
		print(file)
		job_desc = file.split('.')[0]
		d = 'protein'
		os.system('run_pasta.py -i {} -d {} -j {}'.format(file, d, job_desc))
