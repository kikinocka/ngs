#!/usr/bin/env python3
#check spliting sequence name (3x)
import os
from Bio import AlignIO
from collections import OrderedDict, defaultdict

os.chdir('/Users/kika/ownCloud/blastocrithidia/genes/aa-tRNA-synthetases/20210123-check/mafft/')
files = os.listdir()
ins_results = open('ins.test.txt', 'w')
del_results = open('del.test.txt', 'w')
len_results = open('prot_len.test.txt', 'w')
errors = open('errors.test.txt', 'w')

def find_insertion(aln_file):
	aln = AlignIO.read(aln_file, 'fasta')
	result_list = []
	ins_aln_positions = defaultdict(OrderedDict)
	dash_count = 0
	for i in range(aln.get_alignment_length()):
		column = aln[:, i]
		if '-' in column:
			column_list = [i, column]
			result_list.append(column_list)
	for column in result_list:
		for aa in column[1]:
			if aa == '-':
				dash_count += 1
		for number in range(len(aln)):
			if column[1][number] != '-':
				if dash_count >= len(aln)/2:
					ins_aln_positions[number][column[0]] = 1
				else:
					ins_aln_positions[number][column[0]] = 0
			else:
				ins_aln_positions[number][column[0]] = 0
		dash_count = 0
	return ins_aln_positions
	# print(ins_aln_positions)
	# [0 : [position in aln : 0/1], 1 : [position in aln : 0/1], ..., n : [position in aln : 0/1]]
	# 0/1 = absence/presence of insertion in that position of the alignment

def get_peptides(ins_aln_positions, aln_file):
	aln = AlignIO.read(aln_file, 'fasta')
	c = 0
	result_dict = defaultdict(list)
	del_dict = defaultdict(list)
	# len_dict = defaultdict(list)
	len_dict = {}
	for number in range(len(aln)):
		seq_seq = str(aln[number].seq)
		seq_name = aln[number].description
		ungapped_seq = str(seq_seq).replace('-', '')
		result_dict[seq_name].append(aln_file)
		del_dict[seq_name].append(aln_file)
		seq_len = (seq_name.split(' ')[0:2], len(ungapped_seq))
		# seq_len = (seq_name.split('_')[0], len(ungapped_seq))
		# len_dict[aln_file].append(seq_len)
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
					result = (ins_seq, aln_start+1)
					del_dict[seq_name].append(result)
				else:
					result = (ins_seq, aln_start+1, aln_stop+1)
					result_dict[seq_name].append(result)
			elif pos_list[position] + 1 != pos_list[position + 1]:
				stop = int(pos_list[position])
				ins_seq = ungapped_seq[start:stop+1]
				aln_stop = int(aln_pos_list[position])
				if aln_stop == aln_start:
					result = (ins_seq, aln_start+1)
					del_dict[seq_name].append(result)
				else:
					result = (ins_seq, aln_start+1, aln_stop+1)
					result_dict[seq_name].append(result)
		c += 1
	len_dict[aln_file] = aln.get_alignment_length()
	return result_dict, del_dict, len_dict
	#result_dict
	#prot_name : [file_name, (ins_seq, aln_start,aln_stop), (ins_seq, aln_start,aln_stop)]
	#									ins1		   				ins2
	#del_dict
	#prot_name : [file_name, (ins_seq, aln_pos), (ins_seq, aln_pos)]

all_len = {}
for file in files:
	if file.endswith('.aln'):
		try:
			print(file)
			file_name = file.split('.')[0]
			ins_aln_positions = find_insertion(file)
			result_dict = get_peptides(ins_aln_positions, file)[0]
			del_dict = get_peptides(ins_aln_positions, file)[1]
			len_dict = get_peptides(ins_aln_positions, file)[2]
			all_len.update(len_dict)
		# except:
		# 	pass

			for key, value in result_dict.items():
				sp_name = key.split(' ')[0:2]
				# sp_name = key.split('_')[0]
				for i in value[1:]:
					ins_results.write('>{}__{} length_{} pos_{}-{}\n{}\n'.format(file_name, sp_name, len(i[0]),
						i[1], i[2], i[0]))
		
			for key, value in del_dict.items():
				sp_name = key.split(' ')[0:2]
				# sp_name = key.split('_')[0]
				for i in value[1:]:
					del_results.write('>{}__{} {}\n{}\n'.format(file_name, sp_name, i[1], i[0]))
		except ValueError:
			errors.write(file + '\n')

# result_len = {}
# for key, value in all_len.items():
# 	for sp in value:
# 		if sp[0] in result_len.keys():
# 			result_len[sp[0]] += sp[1]
# 		else:
# 			result_len[sp[0]] = sp[1]

# for key, value in result_len.items():
# 	len_results.write('{}\t{}\n'.format(key, value))

result_len = 0
for key, value in all_len.items():
	result_len += value
	len_results.write('{}\t{}\n'.format(key, value))

len_results.write('\nCumulative length of all alignments is: {}\n'.format(result_len))

ins_results.close()
del_results.close()
len_results.close()
errors.close()