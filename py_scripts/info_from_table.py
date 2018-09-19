#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Presequence_classes/')
table = open('monstrozna.tsv')
classI = open('class_I.fa', 'w')
classII = open('class_II.fa', 'w')

for line in table:
	try:
		name = line.split('\t')[0]
		contig = line.split('\t')[2]
		presequence = line.split('\t')[11]
		seq = line.split('\t')[13]
		if presequence == '1':
			classI.write('>{}_{}\n{}\n'.format(contig, name, seq))
		elif presequence == '2':
			classII.write('>{}_{}\n{}\n'.format(contig, name, seq))
		else:
			print(name, contig, presequence)
	except:
		print(line)
