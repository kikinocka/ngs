#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/anaeramoeba/RABs/')
btable = open('Tvag_rev.RABdb.best_blast.tsv')
out = 'Tvag_rev.acc'
rabs = ['Rab', 'IFT', 'Ran', 'RAN', 'RTW', 'Ypt']

with open(out, 'w') as result:
	for line in btable:
		qseqid = line.split('\t')[0]
		sseqid = line.split('\t')[2]
		if any(x in sseqid for x in rabs):
			# print(qseqid, sseqid)
			result.write('{}\n'.format(qseqid))
		else:
			print(qseqid, sseqid)
