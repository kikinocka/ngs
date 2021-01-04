#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/archamoebae/rhizomastix_libera_IND8/')
fasta = SeqIO.parse('Trinity_IND8_010416_renamed_prot.fas', 'fasta')

c = 0
with open('rli_trinity_010416_renamed_prot.fa', 'w') as out:
	for seq in fasta:
		c += 1
		out.write('>rli_{}\n{}\n'.format(seq.description, seq.seq))
		print(c)
