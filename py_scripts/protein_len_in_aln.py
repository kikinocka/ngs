#!/usr/bin/env python3
import os
from Bio import AlignIO

os.chdir('/Dcko/ownCloud/SAGs/phylogenomics/mafft_EU_added/')
files = [x for x in os.listdir() if x.endswith('aln')]
errors = 'corrected/short_seqs.txt'

def seq_cleaner(file):
	with open(errors, 'a') as err:
		print(file)
		seq_dict = {}
		aln = AlignIO.read(file, 'fasta')
		len_aln = aln.get_alignment_length()
		err.write('{}\nalignment length: {} ({})\n'.format(file, len_aln, len_aln/5))

		for seq in aln:
			if 'EU' in seq.name:
				if len(str(seq.seq).replace('-', '')) >= len_aln/5:
					seq_dict[seq.description] = str(seq.seq).replace('-', '')
				else:
					err.write('{} length: {}\n'.format(seq.name, len(str(seq.seq).replace('-', ''))))
		if len(seq_dict) > 0:
			out = open('corrected/{}.fa'.format(file.split('.')[0]), 'w')
			for key, value in seq_dict.items():
					out.write('>{}\n{}\n'.format(key, value))
			for seq in aln:
				if 'EU' in seq.name:
					pass
				else:
					out.write('>{}\n{}\n'.format(seq.name, str(seq.seq).replace('-', '')))
		err.write('======================================\n')

for file in files:
	seq_cleaner(file)
