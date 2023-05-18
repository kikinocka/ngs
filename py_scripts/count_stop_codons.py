#!/usr/bin/env python3
import os
from Bio import SeqIO
from collections import OrderedDict


os.chdir('/Users/kika/data/ciliates/')
files = [x for x in os.listdir() if x.endswith('MMETSP0127_clean.longest_orfs.cds-3end_complete.fna')]



for file in files:
	print(file)
	taa = 0
	tag = 0
	tga = 0
	ambig = {}
	
	out = file.split('_')[0] + '_' + file.split('_')[1] + '.stops.tsv'
	# out = file.split('.')[0] + '.' + file.split('.')[1] + '.stops.tsv'

	with open(out, 'w') as result:
		for seq in SeqIO.parse(file, 'fasta'):
			seq.seq = seq.seq.upper()
			if seq.seq[-3:] == 'TAA':
				taa += 1
			elif seq.seq[-3:] == 'TAG':
				tag += 1
			elif seq.seq[-3:] == 'TGA':
				tga += 1
			else:
				if seq.seq[-3:] not in ambig:
					ambig[seq.seq[-3:]] = 1
				else:
					ambig[seq.seq[-3:]] += 1

		result.write('TAA\t{}\nTAG\t{}\nTGA\t{}\n'.format(taa, tag, tga))
		for key, value in ambig.items():
			result.write('{}\t{}\n'.format(key, value))
