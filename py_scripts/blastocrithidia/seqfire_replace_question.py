#!/usr/bin/env python3
import os

os.chdir('/media/4TB1/blastocrithidia/seqfire/apicomplexans_aln/')
files = sorted(os.listdir())

for file in files:
	if file.endswith('.indel'):
		print(file)
		file_name = file.split('.')[0]
		with open('{}_replaced.indel'.format(file_name), 'w') as out:
			for line in open(file):
				if '?' in line:
					new_line = line.replace('?', 'X')
					out.write(new_line)
				else:
					out.write(line)
