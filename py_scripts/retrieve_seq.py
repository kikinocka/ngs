#!/usr/bin/python3
from Bio import SeqIO

infasta = SeqIO.parse('/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/AA_biosynthetic_pathways/all_aa_Zoli.fasta', 'fasta')
infile = open('/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/AA_biosynthetic_pathways/acc.txt')
out = open('/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/AA_biosynthetic_pathways/contigs.fa', 'w')

retrieve = set()
for line in infile:
	retrieve.add(line[:-1])

for seq in infasta:
	if seq.name in retrieve:
		out.write('>{}\n{}\n'.format(seq.description, seq.seq))
	else:
		print(seq.description)
out.close()