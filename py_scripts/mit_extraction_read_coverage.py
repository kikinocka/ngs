#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/SAGs/assemblies/stats/EU7/tnm/all/qualimap/')
accessions = open('mit.acc')
coverage = open('all_coverage.txt')

acc = set()
for line in accessions:
	acc.add(line[:-1])
print(len(acc))

with open('mit_coverage.txt', 'w') as mito, open('nuc_coverage.txt', 'w') as nuc:
	for line in coverage:
		if line.split('\t')[0] in acc:
			mito.write(line)
		else:
			nuc.write(line)
