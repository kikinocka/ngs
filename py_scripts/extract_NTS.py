#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/pelomyxa_schiedti/nts_charge/')
xls = open('to_cut.tsv')

with open('pelo_nts20.fa', 'w') as out:
	for line in xls:
		name = line.split('\t')[0]
		seq = line.split('\t')[1]
		cut = int(line.split('\t')[2])
		out.write('>{}\n{}\n'.format(name, seq[:20]))
