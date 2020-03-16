#!/usr/bin/env python3
import os

os.chdir('/Dcko/ownCloud/membrane-trafficking/rhynchopus_humris_1608/')
btable = open('rhRABs_rev.best_blast.tsv')
out = 'rhRABs.rev_hits.acc'
rabs = ['Rab', 'IFT27', 'IFT22' 'Ran', 'RAN', 'RTW']

with open(out, 'w') as result:
	for line in btable:
		qseqid = line.split('\t')[0].split(' ')[0]
		sseqid = line.split('\t')[2]
		if any(x in sseqid for x in rabs):
			result.write('{}\n'.format(qseqid))
		else:
			print(sseqid)
