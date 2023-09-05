#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/blasto_comparative/proteins/')
gff = open('Ovol_companion.gff3')
accfile = open('ovol_less30.acc')
out = 'Ovol_companion_l30.gff3'

accessions = []
for acc in accfile:
	accessions.append(acc.split(' ')[0].split('.')[0])
# print(accessions)

with open(out, 'w') as result:
	for line in gff:
		if line.startswith('#'):
			result.write(line)
		else:
			if line.split('\t')[-1].split('=')[1].split(';')[0] in accessions: #gene
				pass
			elif line.split('\t')[-1].split('=')[1].split('.')[0] in accessions: #mRNA, CDS, polypeptide, protein_match
				pass
			else:
				result.write(line)
