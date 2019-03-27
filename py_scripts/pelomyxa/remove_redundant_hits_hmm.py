#!/usr/bin/env python3
import os
from Bio import SeqIO
from collections import OrderedDict

os.chdir('/home/kika/ownCloud/pelomyxa/mito_proteins/transport/tom-tim/hmm/')
files = [x for x in os.listdir() if x.endswith('Tom70.hmm_hits.fa')]

for file in files:
	print(file)
	seq_d = OrderedDict()
	f = SeqIO.parse(file, 'fasta')
	for seq in f:
		seqname = seq.name.split('_')[1]
		if seqname not in seq_d.keys():
			seq_d[seqname] = seq.seq
		else:
			pass
	
	newfile = file.replace('.fa', '_deduplicated.fa')
	with open(newfile, 'w') as result:
		for key, value in seq_d.items():
			result.write('>{}\n{}\n'.format(key, value))
