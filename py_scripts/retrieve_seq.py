#!/usr/bin/env python3
from Bio import SeqIO

infasta = SeqIO.parse('/home/kika/programs/blast-2.5.0+/bin/eg_tsa_Field.fasta', 'fasta')
infile = open('/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/EG_prot/yoshida_dataset/gefr_acc.txt')
out = open('/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/EG_prot/yoshida_dataset/gefr_seqs.fa', 'w')

retrieve = set()
for line in infile:
	retrieve.add(line[:-1])

for seq in infasta:
	if seq.name in retrieve:
		out.write('>{}\n{}\n'.format(seq.description, seq.seq))
	else:
		print(seq.description)
out.close()