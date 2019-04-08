#!/usr/bin/env python3
import os
from Bio import SeqIO
from collections import OrderedDict

os.chdir('/home/kika/ownCloud/blastocrithidia/seqfire/ins_non-ins/')

def count_aa(file, out):
	print(file)
	aa_all = OrderedDict([('len',0),
				('A',0), ('R',0), ('N',0), ('D',0), ('C',0), ('Q',0), ('E',0), ('G',0), ('H',0), ('I',0), ('L',0), 
				('K',0), ('M',0), ('F',0), ('P',0), ('S',0), ('T',0), ('W',0), ('Y',0), ('V',0), ('X',0)])
	# all_len = 0
	with open(out, 'w') as result:
		result.write('\tlength\tA\tR\tN\tD\tC\tQ\tE\tG\tH\tI\tL\tK\tM\tF\tP\tS\tT\tW\tY\tV\tX\n')
		for seq in SeqIO.parse(file, 'fasta'):
			aa = OrderedDict([('len',0),
				('A',0), ('R',0), ('N',0), ('D',0), ('C',0), ('Q',0), ('E',0), ('G',0), ('H',0), ('I',0), ('L',0), 
				('K',0), ('M',0), ('F',0), ('P',0), ('S',0), ('T',0), ('W',0), ('Y',0), ('V',0), ('X',0)])
			for i in seq:
				if i in aa.keys():
					aa[i] += 1
					aa_all[i] += 1
				else:
					print('{} error'.format(seq.description))
			length = len(seq.seq)
			aa['len'] = length
			aa_all['len'] += length
			result.write('{}\t'.format(seq.description))
			for key, value in aa.items():
				result.write('{}\t'.format(value))
			result.write('\n')
		for key, value in aa_all.items():
			result.write('\t{}'.format(value))

def combine_last_rows(tables, out):
	with open(out, 'w') as result:
		result.write('\tlength\tA\tR\tN\tD\tC\tQ\tE\tG\tH\tI\tL\tK\tM\tF\tP\tS\tT\tW\tY\tV\tX\n')
		for table in tables:
			sp = table.split('_aa_counts.tsv')[0].replace('_', ' ')
			lines = open(table).readlines()
			result.write('{} {}\n'.format(sp, lines[-1]))

insertions = [x for x in os.listdir() if x.endswith('.fa')]
for file in insertions:
	sp = file.split('.')[0]
	out = '{}_aa_counts.tsv'.format(sp)
	count_aa(file, out)

tables = [x for x in sorted(os.listdir()) if x.endswith('.tsv')]
result = 'aa_composition.tsv'
combine_last_rows(tables, result)
