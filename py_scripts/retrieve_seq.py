#!/usr/bin/env python3
from Bio import SeqIO

infasta = SeqIO.parse('/home/kika/programs/blast-2.5.0+/bin/CAM_P_0001000.pep.fa', 'fasta')
infile = open('/home/kika/MEGAsync/diplonema/octopine_superfamily/MMETSP_dp_ocdh.dmnd.acc.out')
out = open('/home/kika/MEGAsync/diplonema/octopine_superfamily/MMETSP_dp_ocdh.dmnd.prot.out', 'w')

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
