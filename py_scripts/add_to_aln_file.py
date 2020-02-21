#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Dcko/ownCloud/SAGs/phylogenomics/Bordor-alignments_euglenids-July2019/')
alignments = [x for x in os.listdir() if x.endswith('.faa')]
gproteins = [x for x in os.listdir() if x.endswith('EU1718.fas')]
dproteins = SeqIO.parse('EU1718_david.fasta', 'fasta')

dprots = {}
for protein in dproteins:
	dprots[protein.name.split('_')[1].split('@')[0]] = str(protein.seq)

gprots = {}
for protein in gproteins:
	for seq in SeqIO.parse(protein, 'fasta'):
		gprots[protein.split('_')[0]] = str(seq.seq)

for aln in alignments:
	if aln.split('.')[0] in gprots:
		print(aln + ' in proteins from Gordon')
		print('Adding protein to the alignment')
		with open(aln, 'a') as out:
			out.write('>EU1718g\n{}\n'.format(gprots[aln.split('.')[0]]))
	if aln.split('.')[0] in dprots:
		print(aln + ' in proteins from Gordon')
		print('Adding protein to the alignment')
		with open(aln, 'a') as out:
			out.write('>EU1718d\n{}\n'.format(dprots[aln.split('.')[0]]))
