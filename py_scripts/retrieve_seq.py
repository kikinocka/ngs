#!/usr/bin/env python3
from Bio import SeqIO

infasta = SeqIO.parse('/home/kika/ownCloud/blastocrithidia/genome_assembly/jaculum_scaffolds_transc_translated.fasta', 'fasta')
infile = open('/home/kika/ownCloud/blastocrithidia/ku_story/repair/missing_tryps/in')
out = open('/home/kika/ownCloud/blastocrithidia/ku_story/repair/missing_tryps/jac_rfc1.hmm_hits.fa', 'w')

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
