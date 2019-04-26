#!/usr/bin/env python3
from Bio import SeqIO

infasta = SeqIO.parse('/home/kika/MEGAsync/diplonema_mt/reference_strains/Dp_PB-MI_190104_dedup_cut_l100.faa', 'fasta')
infile = open('/home/kika/ownCloud/blastocrithidia/genes/catalase/diplo/in')
out = open('/home/kika/ownCloud/blastocrithidia/genes/catalase/diplo/dpap_catalase_aa.fa', 'w')

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
