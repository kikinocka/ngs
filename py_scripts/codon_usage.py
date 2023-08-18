#!/usr/bin/env python3
import os
from Bio import SeqIO
from collections import OrderedDict

os.chdir('/Users/kika/ownCloud/blastocrithidia/genes/mtDNA/tryps/')
files = [x for x in os.listdir() if x.endswith('.fa')]

codons = OrderedDict([
		('GCG', 0), ('GCA', 0), ('GCT', 0), ('GCC', 0), ('TGT', 0), ('TGC', 0), ('GAT', 0), ('GAC', 0), ('GAA', 0), 
		('GAG', 0), ('TTT', 0), ('TTC', 0), ('GGG', 0), ('GGA', 0), ('GGT', 0), ('GGC', 0), ('CAT', 0), ('CAC', 0), 
		('ATA', 0), ('ATT', 0), ('ATC', 0), ('AAG', 0), ('AAA', 0), ('TTG', 0), ('TTA', 0), ('CTG', 0), ('CTA', 0), 
		('CTT', 0), ('CTC', 0), ('ATG', 0), ('AAT', 0), ('AAC', 0), ('CCG', 0), ('CCA', 0), ('CCT', 0), ('CCC', 0), 
		('CAG', 0), ('CAA', 0), ('AGG', 0), ('AGA', 0), ('CGG', 0), ('CGA', 0), ('CGT', 0), ('CGC', 0), ('AGT', 0), 
		('AGC', 0), ('TCG', 0), ('TCA', 0), ('TCT', 0), ('TCC', 0), ('ACG', 0), ('ACA', 0), ('ACT', 0), ('ACC', 0), 
		('GTG', 0), ('GTA', 0), ('GTT', 0), ('GTC', 0), ('TGG', 0), ('TAT', 0), ('TAC', 0), ('TAA', 0), ('TAG', 0), 
		('TGA', 0),	('ambig', 0)])

def count_codons(sequence):
	for i in range(0, len(sequence)-2, 3):
		if ('N' in sequence[i:i+3]) or ('W' in sequence[i:i+3]) or ('S' in sequence[i:i+3]) or ('M' in sequence[i:i+3]) or \
		   ('K' in sequence[i:i+3]) or ('R' in sequence[i:i+3]) or ('Y' in sequence[i:i+3]) or ('B' in sequence[i:i+3]) or \
		   ('D' in sequence[i:i+3]) or ('H' in sequence[i:i+3]) or ('V' in sequence[i:i+3]):
			codons['ambig'] += 1
		else:
			codons[sequence[i:i+3].upper()] += 1
	return codons

for file in files:
	print(file)
	table = file.split('.fa')[0] + '.codons.tsv'
	# table = file.split('_')[0] + '_' + file.split('_')[1] + '.codons.tsv'
	# table = file.split('.')[0] + '.' + file.split('.')[1] + '.codons.tsv'
	with open(table, 'w') as result:
		result.write('\tAla\t\t\t\tCys\t\tAsp\t\tGlu\t\tPhe\t\tGly\t\t\t\tHis\t\tIle\t\t\tLys\t\tLeu\t\t\t\t\t\tMet\tAsn\t\tPro\t\t\t\tGln\t\tArg\t\t\t\t\t\tSer\t\t\t\t\t\tThr\t\t\t\tVal\t\t\t\tTrp\tTyr\t\tSTOP\n')
		for key in codons.keys():
			result.write('\t' + key)
		result.write('\n')

		for sequence in SeqIO.parse(file, 'fasta'):
			# print(sequence.name)
			numbers = []

			# #sequence without stops
			# codons = count_codons(sequence.seq)

			#sequence containing stops
			codons = count_codons(sequence.seq[:-3])

			for value in codons.values():
				numbers.append(value)
			result.write('{}'.format(sequence.description))
			for num in numbers:
				result.write('\t' + str(num))
			result.write('\n')
			codons = OrderedDict([(key, 0) for key in codons])
