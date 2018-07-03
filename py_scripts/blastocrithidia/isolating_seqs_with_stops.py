#!/usr/bin/python3
from Bio import SeqIO

infile = SeqIO.parse('/home/kika/Dropbox/blastocrithidia/datasets/aa_ref_for_blasto/p57_aa_from_ref.fasta', 'fasta')
output1 = open('/home/kika/Dropbox/blastocrithidia/datasets/aa_ref_for_blasto/p57_aa_from_ref_with_stops.fasta', 'w')
output2 = open('/home/kika/Dropbox/blastocrithidia/datasets/aa_ref_for_blasto/p57_aa_from_ref_without_stops.fasta', 'w')

for sequence in infile:
	seq = sequence.seq
	name = sequence.name

	if ('+' in seq) or ('#' in seq) or ('*' in seq):
		output1.write('>{}\n{}\n'.format(name, seq))
	else:
		output2.write('>{}\n{}\n'.format(name, seq))

output1.close()
output2.close()