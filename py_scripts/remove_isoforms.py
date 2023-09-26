#!/usr/bin/env python3

#courtesy of github.com/morpholino

import sys
from Bio import SeqIO
import re

#usage python remove_isoforms.py infile [outfile]

infile = sys.argv[1]
if len(sys.argv) > 2:
	outfile = sys.argv[2]
else:
	outfile = '.'.join(infile.split('.')[:-1]) + '-best-isoforms.fasta'

print(f'parsing sequences from {infile} to {outfile}')
isoformRe = re.compile(r'(.*)_i(\d+).*$')

isoforms = {}

with open(outfile, 'wt') as result:
	for seq in SeqIO.parse(infile, 'fasta'):
		match = isoformRe.search(seq.name)
		if match:
			gene, isoform = match.group(1), int(match.group(2))
			if gene in isoforms:
				if isoform < isoforms[gene]:
					isoforms[gene] = isoform
			else:
				isoforms[gene] = isoform

		else:
			print('could not find isoform pattern:', seq.name)

	for seq in SeqIO.parse(infile, 'fasta'):
		match = isoformRe.search(seq.name)
		if match:
			gene, isoform = match.group(1), int(match.group(2))
			if isoform == isoforms[gene]:
				result.write(f'>{seq.description}\n{seq.seq}\n')
