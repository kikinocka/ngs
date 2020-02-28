#!/usr/bin/python3
import os
from Bio import SeqIO

os.chdir('/Dcko/ownCloud/membrane-trafficking/diplonema_papillatum/')
db = SeqIO.parse('/Dcko/MEGAsync/Data/dpapilatum/dpap_predicted_proteins.fa', 'fasta')
accessions = open('dp_RABs.acc')
out = open('dp_RABs.fa', 'w')

retrieve = set()
for line in accessions:
	retrieve.add(line[:-1])

for seq in db:
	if seq.name in retrieve:
		out.write('>{}\n{}\n'.format(seq.description, seq.seq))
	else:
		# print(seq.description)
		pass
out.close()
