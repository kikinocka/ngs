#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/SL_Euglenozoa/V9/supergroups/')

#to remove Metazoa
table = open('Obazoa.tsv')
with open('Obazoa.no_Metazoa.tsv', 'w') as out:
	for line in table:
		if 'Metazoa' in line:
		# if 'Embryophyceae' in line:
			pass
		else:
			out.write(line)


#to remove Embryophyceae
table = open('Archaeplastida.tsv')
with open('Archaeplastida.no_Embryophyceae.tsv', 'w') as out:
	for line in table:
		if 'Embryophyceae' in line:
			pass
		else:
			out.write(line)