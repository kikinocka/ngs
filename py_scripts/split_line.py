#!/usr/bin/env python3
import os

os.chdir('/Users/kika/')
lookup = open('eukprot.lookup', 'r')

with open('eukprot.taxidmapping', 'w') as out:
	for line in lookup:
		accession = line.split('\t')[1]
		taxid = accession.split('|')[-1]
		out.write('{}\t{}\n'.format(accession, taxid))
