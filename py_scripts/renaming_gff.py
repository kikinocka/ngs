#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/blasto_comparative/proteins/companion/Omod/')
gff = open('test.gff')
accfile = open('accessions_conversion.txt')
out = 'test_out.gff'

accessions = {}
for line in accfile:
	accessions[line.split('\t')[0]] = line.strip().split('\t')[1]
# print(accessions)

with open(out, 'w') as result:
	for line in gff:
		for key in accessions:
			line.replace(key, accessions[key])
		result.write(line)
