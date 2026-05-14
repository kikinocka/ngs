#!/usr/bin/env python3
import os
from Bio import SeqIO
from collections import defaultdict

os.chdir('/Users/kika/ownCloud/membrane-trafficking/dicty_JPP/trees/RABs/')
infile = 'rabs.fa'


# for seq in SeqIO.parse(infile, 'fasta'):
# 	with open('{}_query.faa'.format(seq.name), 'w') as result:
# 		# print(str(result))
# 		result.write('>{}\n{}\n'.format(seq.description, seq.seq))


spp = defaultdict(dict)
for seq in SeqIO.parse(infile, 'fasta'):
	orgn = seq.name.split('__')[0].split('_')[0][:1] + seq.name.split('__')[0].split('_')[1][:3]
	spp[orgn][seq.name] = str(seq.seq)

# print(spp)

for key, value in spp.items():
	with open('{}.fa'.format(key), 'w') as result:
		for name, sequence in value.items():
			result.write('>{}\n{}\n'.format(name, sequence))