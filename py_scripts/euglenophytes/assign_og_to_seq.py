#!/usr/bin/env python3
import os
import re
from collections import OrderedDict

os.chdir('/home/kika/ownCloud/euglenophytes/pt_proteome/')
file = open('groups41db_only_euglenids_containing.txt')

with open('og-Rhab_db.tsv', 'w') as result:
	for line in file:
		f = line.split(':')[0]
		names = line.rstrip('\n').split(':')[1].split(' ')
		for i in names:
			if 'DErc' in i:
				result.write('{}\t{}\n'.format(i, f))
