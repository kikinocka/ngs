#!/usr/bin/python3
from Bio import AlignIO
from Bio import SeqIO
import os

out_p57 = open('/home/kika/Dropbox/blastocrithidia/genes/insertions/alignments/out_p57.fasta', 'w')
out_triat = open('/home/kika/Dropbox/blastocrithidia/genes/insertions/alignments/out_triat.fasta', 'w')
out_BexLH = open('/home/kika/Dropbox/blastocrithidia/genes/insertions/alignments/out_BexLH.fasta', 'w')

def get_sequence_number(file):
	sequences = SeqIO.parse(file, 'fasta')
	number = 0
	p57_triat_BexLH = [None, None, None]
	for sequence in sequences:
		if ('p57' not in sequence.name and 'triat' not in sequence.name and 
			'BexLH' not in sequence.name):  
			number +=1
		elif 'p57' in sequence.name:
			p57_triat_BexLH[0] = number
			number +=1
		elif 'triat' in sequence.name:
			p57_triat_BexLH[1] = number
			number +=1
		elif 'BexLH' in sequence.name:
			p57_triat_BexLH[2] = number
			number +=1
	return p57_triat_BexLH

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
					peptide = table[i][positions[seq_index]]
					col_num = int(table[i][-1])
			if seq_index == 0:
				alignment = AlignIO.read(alignment_file, 'fasta')
				for seq in alignment:
					seq_name = seq.name
					if 'p57' in seq_name:
						c = 0
						for i in p57:
							c += 1
							out_p57.write('>{}_{}\n{}\n'.format(seq_name[4:], c, i))
			elif seq_index == 1:
				alignment = AlignIO.read(alignment_file, 'fasta')
				for seq in alignment:
					seq_name = seq.name
					if 'triat' in seq_name:
						c = 0
						for i in triat:
							c += 1
							out_triat.write('>{}_{}\n{}\n'.format(seq_name[6:], c, i))
			elif seq_index == 2:
				alignment = AlignIO.read(alignment_file, 'fasta')
				for seq in alignment:
					seq_name = seq.name
					if 'BexLH' in seq_name:
						c = 0
						for i in BexLH:
							c += 1
							out_BexLH.write('>{}_{}\n{}\n'.format(seq_name[6:], c, i))


os.chdir('/home/kika/Dropbox/blastocrithidia/genes/insertions/alignments/')
files = os.listdir()

for file in files:
	if '.aln' in file:
		print(file)
		x = find_insertions(file)
		peptides(x, file)
		# out_p57.write()
		# out_triat.write()
		# out_BexLH.write()

out_p57.close()
out_triat.close()
out_BexLH.close()