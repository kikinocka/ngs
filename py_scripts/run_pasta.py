#!/usr/bin/python3
import os

os.chdir('/media/4TB1/blastocrithidia/orthofinder/sc_ogs/stops_replaced/')
files = os.listdir()

for file in files:
	if '.fa' in file:
	# if '.aln' not in file:
		print(file)
		job_desc = file.split('_replaced.fa')[0]
		d = 'protein'
		os.system('run_pasta.py -i {} -d {} -j {}'.format(file, d, job_desc))