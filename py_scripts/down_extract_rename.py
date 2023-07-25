#!/usr/bin/env python3
import os
import pandas as pd


os.chdir('/mnt/mokosz/home/kika/allDB/bacteria/all/')
table = pd.read_excel('database.xlsx', sheet_name='bacteria')
errors = open('errors.txt', 'w')

for index, row in table.iterrows():
	fname = row[4]
	link = row[8]
	unzipped = link.split('/')[-1].split('.gz')[0]
	print(fname)
	# print(link)
	# print(unzipped)

	try:
		os.system('wget {}'.format(link))
		os.system('gzip -d {}.gz'.format(unzipped))
		os.system('mv {} {}'.format(unzipped, fname))
	except:
		errors.write('{}\n'.format(fname))
