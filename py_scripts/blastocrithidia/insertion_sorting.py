#!/usr/bin/python3
from Bio import SeqIO
import os

infile = '/home/kika/Dropbox/blasto_project/blastocrithidia/genes/insertions/alignments/ins_p57_nt.fasta'
folder = '/home/kika/Dropbox/blasto_project/blastocrithidia/genes/insertions/alignments/ins_sort/'

if os.path.exists(folder) == False:
	os.mkdir(folder)
	os.chdir(folder)
else:
	os.chdir(folder)

seq_dict = {}
for sequence in SeqIO.parse(infile, 'fasta'):
	seq_dict[sequence.name] = sequence.seq

result_dict = {}
for sequence in SeqIO.parse(infile, 'fasta'):
	first_codon = str(sequence.seq[:3])
	if first_codon not in result_dict:
		result_dict[first_codon] = [sequence.name]
	else:
		result_dict[first_codon].append(sequence.name)

for codon, names in result_dict.items():
	with open(codon + '.fasta', 'w') as result:
		for name in names:
			result.write('>{}\n{}\n'.format(name, seq_dict[name]))