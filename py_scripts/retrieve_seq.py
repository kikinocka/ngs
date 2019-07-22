#!/usr/bin/env python3
from Bio import SeqIO

infasta = SeqIO.parse('/home/kika/programs/blast-2.5.0+/bin/rcos_derc.fasta', 'fasta')
infile = open('/home/kika/ownCloud/euglenophytes/pt_proteome/Rhab/in')
out = open('/home/kika/ownCloud/euglenophytes/pt_proteome/Rhab/Rhab_pt_hits.fa', 'w')

retrieve = set()
for line in infile:
	retrieve.add(line[:-1])

for seq in infasta:
	if seq.name in retrieve:
		out.write('>{}\n{}\n'.format(seq.description, seq.seq))
	else:
		# print(seq.description)
		pass
out.close()
