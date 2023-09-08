#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/blasto_comparative/no_stop_proteins/')
nostop = open('bfru.tsv')
out = 'bfru_GOnumbers.txt'
ipr = open('/Users/kika/ownCloud/blasto_comparative/proteins/BLASTs+bedcov/Bfru_proteins-final.interpro.tsv')


goterms = {}
for line in ipr:
	if len(line.split('\t')) > 13:
		if line.split('\t')[1] == '':
			pass
		elif line.split('\t')[13] == '-':
			pass
		else:
			goterms[line.split('\t')[0]] = line.split('\t')[13]
	else:
		pass

with open(out, 'w') as result:
	for line in nostop:
		if line.split('\t')[0].split(' ')[0] in goterms:
			result.write('{}\t{}\n'.format(line.split('\t')[0].split(' ')[0], goterms[line.split('\t')[0].split(' ')[0]]))
		else:
			result.write('{}\n'.format(line.split('\t')[0].split(' ')[0]))
