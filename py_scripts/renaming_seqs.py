#!/usr/bin/python3
from Bio import SeqIO

infile = SeqIO.parse('/home/kika/MEGAsync/diplonema_mt/1601/genome_assembly/1601_tadpole.fa', 'fasta')

with open('/home/kika/MEGAsync/diplonema_mt/1601/genome_assembly/1601_tadpole_renamed.fa', 'w') as output:
	for seq in infile:
		desc = seq.description.replace(',', '_').replace('=', '_')
		print(desc)
		output.write('>{}\n{}\n'.format(desc, seq.seq))
