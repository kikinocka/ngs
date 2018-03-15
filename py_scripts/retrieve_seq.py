#!/usr/bin/python3
from Bio import SeqIO

infasta = SeqIO.parse('/home/kika/MEGAsync/Data/EL_RNAseq/20140707_ver._r2013-02-05/EL_merged.fasta', 'fasta')
infile = open('/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/pt_division/HMM/in')
out = open('/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/pt_division/HMM/el_arc3_hit.txt', 'w')

retrieve = set()
for line in infile:
	retrieve.add(line[:-1])

for seq in infasta:
	if seq.name in retrieve:
		print(seq.name)
		out.write('>{}\n{}\n'.format(seq.name, seq.seq))
out.close()