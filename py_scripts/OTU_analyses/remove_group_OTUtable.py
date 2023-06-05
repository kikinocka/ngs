#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/oil_sands/amplicons/18S-V4-2018/above99/')

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
