#!/usr/bin/env python3
import os
from Bio import AlignIO
from collections import OrderedDict, defaultdict

os.chdir('/home/kika/blasto_project/apicomplexans/')
files = os.listdir()
ins_results = open('api_ins_more_than_1.txt', 'w')

def find_insertion(aln_file):
	aln = AlignIO.read(aln_file, 'fasta')
	result_list = []
	ins_aln_positions = defaultdict(dict)
	for i in range(aln.get_alignment_length()):
		column = aln.get_column(i)
		if '-' in column:
			column_list = [i, column]
			result_list.append(column_list)
	for number in range(len(aln)):
		for column in result_list:
			if column[1][number] != '-':
				ins_aln_positions[number][column[0]] = 1
			else:
				ins_aln_positions[number][column[0]] = 0
	return ins_aln_positions
	#[0 : [position in aln : 0/1], 1 : [position in aln : 0/1], ..., n : [position in aln : 0/1]]
	#0/1 = absence/presence of insertion in that position of the alignment

def get_peptides(ins_aln_positions, aln_file):
	aln = AlignIO.read(aln_file, 'fasta')
	c = 0
	result_dict = defaultdict(list)
	for number in range(len(aln)):
		seq_seq = str(aln[number].seq)
		seq_name = aln[number].description
		ungapped_seq = str(seq_seq).replace('-', '')
		result_dict[seq_name].append(aln_file)
		sample = ins_aln_positions[c]
		pos_list = [-2]
		aln_pos_list = [-2]
		for position, value in sample.items():
			if value == 1:
				pos_list.append(position - seq_seq[:position].count('-'))
				aln_pos_list.append(position)
		start = -1
		aln_start = -1
		for position in range(1,len(pos_list)):
			if pos_list[position] - 1 != pos_list[position - 1]:
				start = int(pos_list[position])
				aln_start = int(aln_pos_list[position])
			if position == len(pos_list) - 1:
				stop = int(pos_list[position])
				ins_seq = ungapped_seq[start:stop+1]
				aln_stop = int(aln_pos_list[position])
				if aln_stop == aln_start:
					pass
				else:
					result = (ins_seq, aln_start+1, aln_stop+1)
					result_dict[seq_name].append(result)
			elif pos_list[position] + 1 != pos_list[position + 1]:
				stop = int(pos_list[position])
				ins_seq = ungapped_seq[start:stop+1]
				aln_stop = int(aln_pos_list[position])
				if aln_stop == aln_start:
					pass
				else:
					result = (ins_seq, aln_start+1, aln_stop+1)
					result_dict[seq_name].append(result)
		c += 1
	return result_dict
	#prot_name : [file_name, (aln_start,aln_stop), (aln_start,aln_stop)]
	#								ins1		   			ins2

for file in files:
	if file.endswith('.aln'):
		file_name = file.split('.')[0]
		ins_aln_positions = find_insertion(file)
		result_dict = get_peptides(ins_aln_positions, file)
	for key, value in result_dict.items():
		sp_name = key.split('__')[1]
		for i in value[1:]:
			ins_results.write('>{}__{} ins_{}-{}\n{}\n'.format(file_name, sp_name, i[1], i[2], i[0]))
