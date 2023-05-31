#!/usr/bin/env python3
import os
from Bio import SeqIO
from collections import OrderedDict


os.chdir('/Users/kika/ownCloud/diplonema/seq_data/dpapillatum/Gertraud/')
files = [x for x in os.listdir() if x.endswith('.fna')]



for file in files:
	print(file)
	taa = 0
	tag = 0
	tga = 0
	ambig = {}
	
	out = file.split('.fna')[0] + '.stops.tsv'
	# out = file.split('_')[0] + '_' + file.split('_')[1] + '.stops.tsv'
	# out = file.split('.')[0] + '.' + file.split('.')[1] + '.stops.tsv'

	with open(out, 'w') as result:
		for seq in SeqIO.parse(file, 'fasta'):
			seq.seq = seq.seq.upper()
			if seq.seq[-3:] == 'TAA':
				print(seq.description)
				print(seq.seq[-3:])
				taa += 1
			elif seq.seq[-3:] == 'TAG':
				print(seq.description)
				print(seq.seq[-3:])
				tag += 1
			elif seq.seq[-3:] == 'TGA':
				print(seq.description)
				print(seq.seq[-3:])
				tga += 1
			else:
				print(seq.description)
				print(seq.seq[-3:])
				if seq.seq[-3:] not in ambig:
					ambig[seq.seq[-3:]] = 1
				else:
					ambig[seq.seq[-3:]] += 1

		result.write('TAA\t{}\nTAG\t{}\nTGA\t{}\n'.format(taa, tag, tga))
		for key, value in ambig.items():
			result.write('{}\t{}\n'.format(key, value))
