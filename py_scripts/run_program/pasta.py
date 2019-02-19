#!/usr/bin/python3
import os

# pasta = '/home/nenarokova/tools/pasta_tools/pasta/run_pasta.py'

os.chdir('/home/kika/ownCloud/blastocrithidia/genes/catalase/Tb927.8.6010_heme-response/PASTA/')
files = sorted(os.listdir())

for file in files:
	if file.endswith('.fa'):
	# if '.aln' not in file:
		print(file)
		job_desc = file.split('.fa')[0]
		d = 'protein'
		os.system('run_pasta.py -i {} -d {} -j {}'.format(file, d, job_desc))
