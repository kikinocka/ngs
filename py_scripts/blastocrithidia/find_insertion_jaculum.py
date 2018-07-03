#!/usr/bin/python3
#check parsing the file name in the end of the script
import os
from Bio import AlignIO
from Bio import SeqIO

os.chdir('/home/kika/MEGAsync/blasto_project/genes/insertions/alignments/')
files = os.listdir()

out_p57 = open('/home/kika/MEGAsync/blasto_project/genes/insertions/alignments/out_p57_b.txt', 'w')
out_triat = open('/home/kika/MEGAsync/blasto_project/genes/insertions/alignments/out_triat.txt', 'w')
out_BexLH = open('/home/kika/MEGAsync/blasto_project/genes/insertions/alignments/out_bexlh.txt', 'w')
out_jac = open('/home/kika/MEGAsync/blasto_project/genes/insertions/alignments/out_jac.txt', 'w')
out_len = open('/home/kika/MEGAsync/blasto_project/genes/insertions/alignments/out_len.tsv', 'w')

def get_sequence_number(file):
	sequences = SeqIO.parse(file, 'fasta')
	number = 0
	p57_triat_BexLH_jac = [None, None, None, None]
	for sequence in sequences:
		if ('p57' not in sequence.name and 'triat' not in sequence.name and 
			'BexLH' not in sequence.name and 'jac' not in sequence.name):  
			number +=1
		elif 'p57' in sequence.name:
			p57_triat_BexLH_jac[0] = number
			number +=1
		elif 'triat' in sequence.name:
			p57_triat_BexLH_jac[1] = number
			number +=1
		elif 'BexLH' in sequence.name:
			p57_triat_BexLH_jac[2] = number
			number +=1
		elif 'jac' in sequence.name:
			p57_triat_BexLH_jac[3] = number
			number +=1
	return p57_triat_BexLH_jac

def find_insertions(alignment_file):
	alignment = AlignIO.read(alignment_file, 'fasta')
	positions = (get_sequence_number(alignment_file))
	positive_positions= []
	result_list = []
	for position in positions:
		if position != None:
			positive_positions.append(position)
	for i in range(alignment.get_alignment_length()):
		col = alignment.get_column(i)
		dash_count = col.count('-')
		if dash_count >= len(alignment)-len(positive_positions):
			true_insertions = 0
			for position in positive_positions:
				if col[position] != '-':
					true_insertions += 1
			if true_insertions + dash_count == len(alignment):
				list_col = list(col)
				list_col.append(i)
				result_list.append(list_col)
	return result_list	

def peptides(table, alignment_file):
	positions = (get_sequence_number(alignment_file))
	p57 = []
	triat = []
	BexLH = []
	jac = []
	for pos in positions:
		peptide = ''
		col_num = 0
		if pos != None:
			seq_index = int(positions.index(pos))
			for i in range(len(table)):
				if int(i) == int(len(table))-1:
					peptide += table[i][positions[seq_index]]
					if seq_index == 0:
						p57.append(peptide.replace('-', ''))
					elif seq_index == 1:
						triat.append(peptide.replace('-', ''))
					elif seq_index == 2:
						BexLH.append(peptide.replace('-', ''))
					elif seq_index == 3:
						jac.append(peptide.replace('-', ''))
				elif table[i][positions[seq_index]] != '-' and len(peptide) < 1:
					peptide = table[i][positions[seq_index]]
					col_num = int(table[i][-1])
				elif int(table[i][-1]) == col_num + 1:
					peptide += table[i][positions[seq_index]]
					col_num = table[i][-1]
					col_num = int(table[i][-1])
				elif table[i][positions[seq_index]] != '-' and int(table[i][-1] != col_num + 1):
					if seq_index == 0:
						p57.append(peptide.replace('-', ''))
					elif seq_index == 1:
						triat.append(peptide.replace('-', ''))
					elif seq_index == 2:
						BexLH.append(peptide.replace('-', ''))
					elif seq_index == 3:
						jac.append(peptide.replace('-', ''))
					peptide = table[i][positions[seq_index]]
					col_num = int(table[i][-1])
			if seq_index == 0:
				alignment = AlignIO.read(alignment_file, 'fasta')
				for seq in alignment:
					seq_name = seq.name
					if 'p57' in seq_name:
						out_p57.write('>' + seq_name + '\n')
						out_len.write('p57\t')
						for i in p57:
							length = str(len(i))
							out_p57.write(i + '\n')
							out_len.write(length + ', ')
						out_len.write('\n')
			elif seq_index == 1:
				alignment = AlignIO.read(alignment_file, 'fasta')
				for seq in alignment:
					seq_name = seq.name
					if 'triat' in seq_name:
						out_triat.write('>' + seq_name + '\n')
						out_len.write('triat\t')
						for i in triat:
							length = str(len(i))
							out_triat.write(i + '\n')
							out_len.write(length + ', ')
						out_len.write('\n')
			elif seq_index == 2:
				alignment = AlignIO.read(alignment_file, 'fasta')
				for seq in alignment:
					seq_name = seq.name
					if 'BexLH' in seq_name:
						out_BexLH.write('>' + seq_name + '\n')
						out_len.write('BexLH\t')
						for i in BexLH:
							length = str(len(i))
							out_BexLH.write(i + '\n')
							out_len.write(length + ', ')
						out_len.write('\n')
			elif seq_index == 3:
				alignment = AlignIO.read(alignment_file, 'fasta')
				for seq in alignment:
					seq_name = seq.name
					if 'jac' in seq_name:
						out_jac.write('>' + seq_name + '\n')
						out_len.write('jac\t')
						for i in jac:
							length = str(len(i))
							out_jac.write(i + '\n')
							out_len.write(length + ', ')
						out_len.write('\n')

for file in files:
	if '.aln' in file:
		print(file)
		out_p57.write(file.split('.m')[0] + '\n')
		out_triat.write(file.split('.m')[0] + '\n')
		out_BexLH.write(file.split('.m')[0] + '\n')
		out_jac.write(file.split('.m')[0] + '\n')
		out_len.write('\t' + file.split('.m')[0] + '\n')
		x = find_insertions(file)
		peptides(x, file)
		out_p57.write('\n')
		out_triat.write('\n')
		out_BexLH.write('\n')
		out_jac.write('\n')
		out_len.write('\n')

out_p57.close()
out_triat.close()
out_BexLH.close()
out_jac.close()
out_len.close()