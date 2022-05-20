#!/usr/bin/env python3
import os

os.chdir('/Users/kika/data/eggnog/')
file = open('eggnog_ogs_dupl.txt')

unique = set()
for line in file:
	if line not in unique:
		unique.add(line)
	else:
		pass

with open('eggnog_ogs.txt', 'w') as out:
	for item in unique:
		out.write(item)
