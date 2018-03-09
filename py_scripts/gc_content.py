#!/usr/bin/python3
from Bio import SeqIO

infile = SeqIO.parse('/home/kika/MEGAsync/blasto_project/genes/catalase/nt/ins_nt.fasta', 'fasta')
outfile = open('/home/kika/MEGAsync/blasto_project/genes/catalase/nt/ins_gc.tsv', 'w')

outfile.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format('ins', 'ins length [# nt]', 'A [# nt]', 
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
	seq = sequence.seq.upper()
	name = sequence.description
	outfile.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(name, len(seq), calculator(seq)[0], 
		calculator(seq)[1], calculator(seq)[2], calculator(seq)[3], calculator(seq)[4], calculator(seq)[5], 
		calculator(seq)[6]))
outfile.close()