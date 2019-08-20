#!/usr/bin/python3
from Bio import SeqIO

infile = SeqIO.parse('/home/kika/mapping/blasto/blasto_mapping/p57_pilon/p57_pilon5.fa', 'fasta')

with open('/home/kika/ownCloud/blastocrithidia/genome_assembly/p57_polished.fa', 'w') as output:
	for seq in infile:
		desc = '{}_length_{}'.format(seq.description.split('_')[0], len(seq.seq))
		print(desc)
		output.write('>{}\n{}\n'.format(desc, seq.seq))
