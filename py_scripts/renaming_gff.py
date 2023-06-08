#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/blastocrithidia/transcriptome_assembly/')
gff = open('p57_cufflinks.gtf')
accfile = open('full_scaffold_names.txt')
out = 'p57_cufflinks.renamed.gtf'

accessions = {}
for line in accfile:
	accessions[line.split('\t')[0]] = line.strip().split('\t')[1]
# print(accessions)

with open(out, 'w') as result:
	for line in gff:
		for key in accessions:
			line = line.replace(key, accessions[key])
		result.write(line)
