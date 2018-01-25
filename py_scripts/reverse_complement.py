#!/usr/bin/python3
from Bio import SeqIO

infile = SeqIO.parse('/home/kika/Dropbox/blasto_project/blastocrithidia/genes/mt/t-aligner_dataset/extended_100/extended_100_2.fasta', 'fasta')
outfile = open('/home/kika/Dropbox/blasto_project/blastocrithidia/genes/mt/t-aligner_dataset/extended_100/extended_100.fasta', 'w')

for sequence in infile:
	desc = sequence.description
	seq = sequence.seq
	if 'reverse' in desc:
		outfile.write('>{}\n{}\n'.format(desc, seq.reverse_complement()))
	else:
		outfile.write('>{}\n{}\n'.format(desc, seq))
outfile.close()		