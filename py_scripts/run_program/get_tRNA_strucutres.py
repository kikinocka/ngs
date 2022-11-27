#!/usr/bin/env python3
import os


os.chdir('/Users/kika/ownCloud/blastocrithidia/genes/tRNAs/ciliates/structures')
files = [x for x in os.listdir() if x.endswith('.txt')]


for file in files:
	print(file)
	name = file.split('.aragorn')[0]
	out = '{}.tRNA-Gln.txt'.format(name)
	os.system('grep -B30 "tRNA-Gln" {} > {}'.format(file, out))
