#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/blastocrithidia/predicted_proteins/')
infile = SeqIO.parse('bnon.no_mtDNA.CDS_cdseq.fna', 'fasta')
outfile = open('bnon.no_mtDNA.CDS_cdseq.GC_content.tsv', 'w')

outfile.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format('seq', 'seq length [# nt]', 'A [# nt]', 
	'T [# nt]', 'C [# nt]', 'G [# nt]', 'ambiguous [# nt]', 'GC content [%]', 'AT content [%]'))

def calculator(sequence):
	ambiguous = 0
	T = sequence.count('T')
	A = sequence.count('A')
	C = sequence.count('C')
	G = sequence.count('G')
	for i in sequence:
		if i not in 'TACG':
			ambiguous += 1
	if (G+C+A+T) != 0:
		GC_content = round((G+C)*100/(G+C+A+T), 2)
		AT_content = 100 - GC_content
	else:
		GC_content = 'NA'
		AT_content = 'NA'
	return A, T, C, G, ambiguous, GC_content, AT_content

for sequence in infile:

	#not to count stops in GC content
	if sequence.seq[-3:] in ['TAA', 'TAG', 'TGA']:
		seq = sequence.seq[:-3].upper()
	else:
		seq = sequence.seq.upper()

	print(sequence.name)
	outfile.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(sequence.description, len(seq), calculator(seq)[0], 
		calculator(seq)[1], calculator(seq)[2], calculator(seq)[3], calculator(seq)[4], calculator(seq)[5], 
		calculator(seq)[6]))
outfile.close()
