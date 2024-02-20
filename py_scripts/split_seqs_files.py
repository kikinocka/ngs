#!/usr/bin/env python3
import os
from Bio import SeqIO


os.chdir('/Users/kika/ownCloud/blasto_comparative/genes/ribosomal_proteins/')

for seq in SeqIO.parse('mito.fa', 'fasta'):
	with open('queries/{}.faa'.format(seq.name), 'w') as result:
		result.write('>{}\n{}\n'.format(seq.description, seq.seq))
