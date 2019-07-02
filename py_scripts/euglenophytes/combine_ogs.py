#!/usr/bin/env python3
import os
import re

os.chdir('/home/kika/ownCloud/euglenophytes/pt_proteome/')
table = open('all_comparison.txt')

with open('ogs_to_join.txt', 'w') as out:
	for line in table:
		matches = set()
		for match in re.finditer('q2\d+', line):
			matches.add(match.group())
	
		if len(matches) == 1:
			pass
		else:		
			for i in matches:
				out.write('{}\t'.format(i))
			out.write('\n')
