#!/usr/bin/python3
from Bio import SeqIO

infile = SeqIO.parse('/home/kika/MEGAsync/Chlamydomonas/Cre_pt.txt', 'fasta')
output = open('/home/kika/MEGAsync/Chlamydomonas/Cre_pt_renamed.txt', 'w')

for sequence in infile:
	name = sequence.description.split('prot_')[1].split(' [protein=')[0].replace(' [gene=', '_').replace(']', '')
	seq = sequence.seq
	output.write('>{}\n{}\n'.format(name, seq))
output.close()