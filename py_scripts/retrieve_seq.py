#!/usr/bin/python3
from Bio import SeqIO

hits = open('/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/srp/HMM/in')

with open('/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/srp/HMM/out', 'w') as res:
	for line in hits:
		for contig in SeqIO.parse('/home/kika/MEGAsync/Data/EG_RNAseq/EGALL_6frames.fasta', 'fasta'):
			if contig.name == line[:-1]:
				res.write('>{}\n{}\n'.format(contig.description, contig.seq))
