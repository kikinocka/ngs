#!/usr/bin/python3
import os
from Bio import SeqIO

os.chdir('/Dcko/ownCloud/SAGs/phylogenomics/EU1718/')
db = SeqIO.parse('dbeuEU1718.fas', 'fasta')
accessions = open('eu1718_found.acc')
out = open('eu1718_found.fa', 'w')

retrieve = set()
for line in accessions:
	retrieve.add(line[:-1])

for seq in db:
	if seq.name in retrieve:
		out.write('>{}\n{}\n'.format(seq.name, seq.seq))
	else:
		# print(seq.description)
		pass
out.close()
