#!/usr/bin/env python3
import os

os.chdir('/home/kika/ownCloud/euglenophytes/pt_proteome/groups/')
files = [x for x in os.listdir() if 'og' in x]

for file in files:
	print(file)
	out = file.split('.')[0] + '_sorted.tsv'
	with open(out, 'w') as result:
		for line in open(file):
			items = line.strip().split(', ')
			items.sort()
			for i in items:
				result.write('{}\t'.format(i))
			result.write('\n')
