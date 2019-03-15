#!/usr/bin/env python3

accessions = 'prot.accession2taxid'
not_tax = 'pelo_trinity.not_taxified.out'
taxified = 'pelo_trinity.taxified.out'

renamekey = {}
with open(accessions) as f:
	for l in f:
		line = l.strip().split('\t')
		renamekey[line[1]] = line[2]

renameset = set(renamekey.keys())

with open(not_tax) as f, open(taxified, 'w') as out:
	for l in f:
		hit = l.strip().split('\t')[-1]
		if hit in renameset:
			out.write(l.replace('N/A', renamekey[hit]))
		else:
			out.write(l)
