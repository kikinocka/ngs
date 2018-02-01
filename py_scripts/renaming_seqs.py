#!/usr/bin/python3
from Bio import SeqIO

infile = SeqIO.parse('/home/kika/MEGAsync/blasto_project/blast_searches/bexlh1/bexlh1_aa_SLremoved.fa', 'fasta')

i = 1
with open('/home/kika/MEGAsync/blasto_project/blast_searches/bexlh1/bexlh1_aa_renamed.fa', 'w') as output:
	for sequence in infile:
		print(sequence.description)
		contig = sequence.description.split('__')[0]
		unique = sequence.description.split('__')[1]
		if i < 10:
			name = 'Btri_0000{} {} {}'.format(i, unique, contig)
		elif i < 100:
			name = 'Btri_000{} {} {}'.format(i, unique, contig)
		elif i < 1000:
			name = 'Btri_00{} {} {}'.format(i, unique, contig)
		else:
			name = 'Btri_0{} {} {}'.format(i, unique, contig)
		i += 1
		output.write('>{}\n{}\n'.format(name, sequence.seq))
