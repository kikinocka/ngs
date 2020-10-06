#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/pelomyxa_schiedti/pasa-evm/')
gff = open('test.gff')

genes = []
for line in gff:
	if line == '###\n':
		pass
	else:
		if line.split('\t')[2] == 'gene':	
			gene = line.split('\t')[8].split('ID=')[1].split(';')[0]
			genes.append(gene)
