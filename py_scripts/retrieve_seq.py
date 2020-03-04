#!/usr/bin/python3
import os
from Bio import SeqIO

os.chdir('/Dcko/ownCloud/membrane-trafficking/rhynchopus_humris_1608/')
db = SeqIO.parse('/Dcko/MEGAsync/Data/diplonemids_transcriptomes/1608_Trinity.fasta', 'fasta')
accessions = open('rhRABs_hits.acc')
out = open('rhRABs_hits.fa', 'w')

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
