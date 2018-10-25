#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/home/kika/ownCloud/blastocrithidia/genes/glycolysis/PASTA/')
p57 = SeqIO.parse('p57_glycolysis_aa.fa', 'fasta')

for seq in p57:
	name = seq.name.split('__')[1]
	file = name + '.fa'
	with open(file, 'a') as result:
		result.write('>{}\n{}\n'.format(seq.description, seq.seq))
