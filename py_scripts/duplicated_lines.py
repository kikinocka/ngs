#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/euglenozoa_mito/mitoribosome/')
file = open('in.acc')

unique = set()
for line in file:
	if line not in unique:
		unique.add(line)
	else:
		pass

with open('in.txt', 'w') as out:
	for item in unique:
		out.write(item)
