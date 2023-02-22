#!/usr/bin/env python3
import os
from Bio import AlignIO

os.chdir('/Users/kika/ownCloud/Gln-tRNA/manual_alns/')
aln = AlignIO.read('uar=stop.mafft.spp_deduplicated.aln', 'fasta')

good_pairs = ['A-T', 'T-A', 'C-G', 'G-C']

for seq in aln:
	pos28 = seq.seq[34]
	pos42 = seq.seq[48]
	pair = pos28 + '-' + pos42
	if pair not in good_pairs:
		print(seq.name, pair)
