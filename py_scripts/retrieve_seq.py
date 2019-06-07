#!/usr/bin/env python3
from Bio import SeqIO

infasta = SeqIO.parse('/home/kika/MEGAsync/Data/EG_RNAseq/EUGR_all.fasta', 'fasta')
infile = open('/home/kika/ownCloud/euglenophytes/plastid_proteome/plastid_proteins_list.txt')
out = open('/home/kika/ownCloud/euglenophytes/plastid_proteome/plastid_proteins.fa', 'w')

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
