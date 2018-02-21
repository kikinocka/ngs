#!/usr/bin/python3
#!!! check parsing file name in the end !!!
import os
import re
from Bio import SeqIO, AlignIO
from collections import defaultdict

p57_genome = '/home/kika/programs/blast-2.5.0+/bin/p57_DNA_scaffolds.fa'
jac_genome = '/home/kika/programs/blast-2.5.0+/bin/jaculum_scaffolds_transc.fasta'

os.chdir('/media/4TB1/blastocrithidia/orthofinder/sg_ogs/alignments/test/')
files = os.listdir()
p57_aa = open('p57_aa.txt', 'w')
p57_nt = open('p57_nt.txt', 'w')
p57_gff = open('p57_insertions.gff', 'w')
p57_errors = open('p57_errors.txt', 'w')
jac_aa = open('jac_aa.txt', 'w')
jac_nt = open('jac_nt.txt', 'w')
jac_gff = open('jac_insertions.gff', 'w')
jac_errors = open('jac_errors.txt', 'w')
gencode = {
	'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
	'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
	'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
	'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
	'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
	'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
	'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
	'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
	'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
	'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
	'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
	'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
	'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
	'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
	'TAC':'Y', 'TAT':'Y', 'TAA':'E', 'TAG':'E',
	'TGC':'C', 'TGT':'C', 'TGA':'W', 'TGG':'W'}

p57_gff.write('{}\t{}\n'.format('##gff-version', '3'))
jac_gff.write('{}\t{}\n'.format('##gff-version', '3'))

def get_seq_number(aln_file):
	sequences = SeqIO.parse(aln_file, 'fasta')
	number = 0
	p57_triat_BexLH_jac = [None, None, None, None]
	for sequence in sequences:
		if ('Bp57' not in sequence.name and 'Btri' not in sequence.name and 
			'Bexl' not in sequence.name and 'Jac' not in sequence.name):  
			number += 1
		elif 'Bp57' in sequence.name:
			p57_triat_BexLH_jac[0] = number
			number += 1
		elif 'Btri' in sequence.name:
			p57_triat_BexLH_jac[1] = number
			number += 1
		elif 'Bexl' in sequence.name:
			p57_triat_BexLH_jac[2] = number
			number += 1
		elif 'Jac' in sequence.name:
			p57_triat_BexLH_jac[3] = number
			number += 1
	return p57_triat_BexLH_jac

def find_insertion(aln_file):
	alignment = AlignIO.read(aln_file, 'fasta')
	seq_numbers = get_seq_number(aln_file)
	seqs_present = []
	result_list = []
	ins_aln_positions = defaultdict(dict)
	for number in seq_numbers:
		if number != None:
			seqs_present.append(number)
	for i in range(alignment.get_alignment_length()):
		ins_aln_positions[0][i] = 0 #p57
		ins_aln_positions[1][i] = 0 #triat
		ins_aln_positions[2][i] = 0 #bexlh
		ins_aln_positions[3][i] = 0 #jac
		column = alignment[:, i]
		dash_count = column.count('-')
		if dash_count >= len(alignment) - len(seqs_present):
			true_insertions = 0
			for seq in seqs_present:
				if column[seq] != '-':
					true_insertions += 1
			if true_insertions + dash_count == len(alignment):
				column_list = list(column)
				column_list.append(i)
				result_list.append(column_list)
	for number in range(len(seq_numbers)):
		if seq_numbers[number] != None:
			for column in result_list:
				if column[seq_numbers[number]] != '-':
					ins_aln_positions[number][column[-1] + 1] = 1
	return ins_aln_positions
	#[0 : [position in aln : 0/1], 1 : [position in aln : 0/1], 2 : [position in aln : 0/1], 3 : [position in aln : 0/1]]
	#0, 1, 2, 3 = p57, triat, bexlh, jac
	#0/1 = absence/presence of insertion in that position of the alignment

def get_peptides(ins_aln_positions, aln_file):
	alignment = AlignIO.read(aln_file, 'fasta')
	seq_numbers = get_seq_number(aln_file)
	p57_triat_BexLH_jac = 0
	names = ['Bp57', 'Btri', 'Bexl', 'Jac']
	result_dict = defaultdict(list)
	for number in seq_numbers:
		if number != None:
			seq_seq = alignment[number].seq
			seq_name = alignment[number].description
			ungapped_seq = str(seq_seq).replace('-', '')
			result_dict[seq_name].append(ungapped_seq)
			result_dict[seq_name].append(aln_file)
			sample = ins_aln_positions[p57_triat_BexLH_jac]
			position_list = [-2]
			for position, value in sample.items():
				if value == 1:
					position_list.append(position - seq_seq[:position].count('-'))
			start = -1
			for position in range(1,len(position_list)):
				if position_list[position] - 1 != position_list[position - 1]:
					start = int(position_list[position])
				if position == len(position_list) - 1:
					stop = int(position_list[position])
					coordinates = (start, stop)
					result_dict[seq_name].append(coordinates)
				elif position_list[position] + 1 != position_list[position + 1]:
					stop = int(position_list[position])
					coordinates = (start, stop)
					result_dict[seq_name].append(coordinates)
		p57_triat_BexLH_jac += 1
	return result_dict
	#[prot_name : (prot_seq, file_name, (start,stop), (start,stop))]
	#									     ins1		   ins2

def translation(nucl_seq):
	cut_seq = []
	for i in range(0,len(nucl_seq)-2, 3):
		cut_seq.append(nucl_seq[i:i+3])
	aa = []
	for codon in cut_seq:
		if 'N' in codon:
			aa.append('X')
		else:
			aa.append(gencode[codon])
	return ''.join(aa)

def orf(species, result_dict, genome):
	contigs = SeqIO.parse(genome, 'fasta')
	proteins_from_aln = result_dict
	sp_contigs = {}
	for contig in contigs:
		sp_contigs[contig.name] = contig.seq
	orf = {}
	not_genome = {}
	no_orf = {}
	for key in proteins_from_aln.keys():
		if species in key:
			key_root = re.sub(r'.*(NODE_\d+_length_\d+_cov_\d+.\d+).*', r'\g<1>', key)
			if key_root in sp_contigs.keys():
				nucl = sp_contigs[key_root]
				reverse = nucl.reverse_complement()
				prot = proteins_from_aln[key][0]
				if str(prot) in translation(nucl):
					orf_start = 3 * (translation(nucl).find(str(prot))) + 1
					orf_end = orf_start + (3 * len(prot)) + 2
					frame = '1'
					orf[key_root] = [nucl[orf_start:orf_end], orf_start, orf_end, frame, proteins_from_aln[key][1]]
				elif str(prot) in translation(nucl[1:]):
					orf_start = 3 * (translation(nucl[1:]).find(str(prot))) + 2
					orf_end = orf_start + (3 * len(prot)) + 2
					frame = '2'
					orf[key_root] = [nucl[orf_start:orf_end], orf_start, orf_end, frame, proteins_from_aln[key][1]]
				elif str(prot) in translation(nucl[2:]):
					orf_start = 3 * (translation(nucl[2:]).find(str(prot))) + 3
					orf_end = orf_start + (3 * len(prot)) + 2
					frame = '3'
					orf[key_root] = [nucl[orf_start:orf_end], orf_start, orf_end, frame, proteins_from_aln[key][1]]
				elif str(prot) in translation(reverse):
					orf_start = 3 * (translation(reverse).find(str(prot)))
					orf_end = orf_start + (3 * len(prot)) + 3
					orf_start_contig = len(reverse) - orf_end + 1
					orf_end_contig = len(reverse) - orf_start
					frame = 'c1'
					orf[key_root] = [reverse[orf_start:orf_end], orf_start_contig, orf_end_contig, frame, proteins_from_aln[key][1]]
				elif str(prot) in translation(reverse[1:]):
					orf_start = 3 * (translation(reverse[1:]).find(str(prot))) + 1
					orf_end = orf_start + (3 * len(prot)) + 3
					orf_start_contig = len(reverse) - orf_end + 1
					orf_end_contig = len(reverse) - orf_start
					frame = 'c2'
					orf[key_root] = [reverse[orf_start:orf_end], orf_start_contig, orf_end_contig, frame, proteins_from_aln[key][1]]
				elif str(prot) in translation(reverse[2:]):
					orf_start = 3 * (translation(reverse[2:]).find(str(prot))) + 2
					orf_end = orf_start + (3 * len(prot)) + 3
					orf_start_contig = len(reverse) - orf_end + 1
					orf_end_contig = len(reverse) - orf_start
					frame = 'c3'
					orf[key_root] = [reverse[orf_start:orf_end], orf_start_contig, orf_end_contig, frame, proteins_from_aln[key][1]]
				else:
					no_orf[proteins_from_aln[key][1]] = key
			else:
				not_genome[proteins_from_aln[key][1]] = key
	return orf, no_orf, not_genome
	#orf
	#contig name : orf sequence 	orf start 	orf end 	frame	file name
	#			   [0]				[1]			[2]			[3]		[4]	

final_dict = {}
p57_no_orf = {}
p57_not_genome = {}
jac_no_orf = {}
jac_not_genome = {}
for file in files:
	if '.aln' in file:
		print(file)
		ins_aln_positions = find_insertion(file)
		result_dict = get_peptides(ins_aln_positions, file)
		final_dict.update(result_dict)
		p57_dict, p57_no_orf, p57_not_genome = orf('Bp57', final_dict, p57_genome)
		jac_dict, jac_no_orf, jac_not_genome = orf('Jac', final_dict, jac_genome)
		# jac_no_orf.update(jac_no_orf)
		# jac_not_genome.update(jac_not_genome)

# print(final_dict)
# print(p57_dict)
# print(p57_no_orf)
# print(p57_not_genome)
# print(jac_no_orf)
# print(jac_not_genome)

p57_errors.write('NO FRAME FOUND:\n')
for key, value in p57_no_orf.items():
	p57_errors.write('{}\t{}'.format(value, key))
	p57_errors.write('\n')
p57_errors.write('\nNOT FOUND IN GENOME:\n')
for key, value in p57_not_genome.items():
	p57_errors.write('{}\t{}'.format(value, key))
	p57_errors.write('\n')

jac_errors.write('NO FRAME FOUND:\n')
for key, value in jac_no_orf.items():
	jac_errors.write('{}\t{}'.format(value, key))
	jac_errors.write('\n')
jac_errors.write('\nNOT FOUND IN GENOME:\n')
for key, value in jac_not_genome.items():
	jac_errors.write('{}\t{}'.format(value, key))
	jac_errors.write('\n')

for key in p57_dict.keys():
	orf_start = p57_dict[key][1]
	orf_end = p57_dict[key][2]
	gene_name = p57_dict[key][4].split('.marker')[0]
	if 'c' not in p57_dict[key][3]:
		p57_gff.write('{}\tblast\tCDS\t{}\t{}\t.\t+\t.\tID={}\n'.format(key, p57_dict[key][1], 
			p57_dict[key][2], p57_dict[key][4].split('.marker')[0]))
		for prot_key in final_dict.keys():
			if len(final_dict[prot_key]) == 2:
				pass
			else:
				key_root = re.sub(r'.*(NODE_\d+_length_\d+_cov_\d+.\d+).*', r'\g<1>', prot_key)
				if key_root == key:
					c = 1
					for i in final_dict[prot_key][2:]:
						if i[0] == 1:
							p57_nt.write('>{}_ins{}\n{}\n'.format(prot_key, c, p57_dict[key][0][i[0]-1:3*i[1]-1]))
						else:
							p57_nt.write('>{}_ins{}\n{}\n'.format(prot_key, c, p57_dict[key][0][3*(i[0]-1)-1:3*i[1]-1]))
						if i[0] == i[1]:
							p57_aa.write('>{}_ins{}\n{}\n'.format(prot_key, c, final_dict[prot_key][0][i[0]-1:i[0]]))
						else:
							p57_aa.write('>{}_ins{}\n{}\n'.format(prot_key, c, final_dict[prot_key][0][i[0]-1:i[1]]))
						ins_start = orf_start + 3 * (i[0] - 1)
						ins_end = ins_start + 3 * (i[1] - i[0] + 1) - 1
						if c == 1:
							ex_start = orf_start
							ex_end = orf_start + 3 * (final_dict[prot_key][2:][c-1][0] - 1) - 1
						else:
							ex_start = orf_start + 3 * final_dict[prot_key][2:][c-2][1]
							ex_end = orf_start + 3 * (final_dict[prot_key][2:][c-1][0] - 1) - 1
						p57_gff.write('{}\tblast\texon\t{}\t{}\t.\t+\t.\tParent={}\n'.format(key, ex_start, ex_end, 
							gene_name))
						p57_gff.write('{}\tblast\tintron\t{}\t{}\t.\t+\t.\tParent={};ID=ins{}\n'.format(key, ins_start, 
							ins_end, gene_name, c))
						c += 1
					try:
						ex_start = orf_start + 3 * int(final_dict[prot_key][-1][1])
						ex_end = orf_end
						p57_gff.write('{}\tblast\texon\t{}\t{}\t.\t+\t.\tParent={}\n'.format(key, ex_start, ex_end, 
							gene_name))
					except:
						pass
	else:
		p57_gff.write('{}\tblast\tCDS\t{}\t{}\t.\t-\t.\tID={}\n'.format(key, p57_dict[key][1], 
			p57_dict[key][2], gene_name))
		for prot_key in final_dict.keys():
			if len(final_dict[prot_key]) == 2:
				pass
			else:
				key_root = re.sub(r'.*(NODE_\d+_length_\d+_cov_\d+.\d+).*', r'\g<1>', prot_key)
				if key_root == key:
					c = 1
					for i in final_dict[prot_key][2:]:
						if i[0] == 1:
							p57_nt.write('>{}_ins{}\n{}\n'.format(prot_key, c, p57_dict[key][0][i[0]-1:3*i[1]]))
						else:
							p57_nt.write('>{}_ins{}\n{}\n'.format(prot_key, c, p57_dict[key][0][3*(i[0]-1):3*i[1]]))
						if i[0] == i[1]:
							p57_aa.write('>{}_ins{}\n{}\n'.format(prot_key, c, final_dict[prot_key][0][i[0]-1:i[0]]))
						else:
							p57_aa.write('>{}_ins{}\n{}\n'.format(prot_key, c, final_dict[prot_key][0][i[0]-1:i[1]]))
						ins_end = orf_end - 3 * (i[0] - 1)
						ins_start = ins_end - 3 * (i[1] - i[0] + 1) + 1
						if c == 1:
							ex_start = orf_end
							ex_end = orf_end - 3 * (final_dict[prot_key][2:][c-1][0] - 1) + 1
						else:
							ex_start = orf_end - 3 * final_dict[prot_key][2:][c-2][1]
							ex_end = orf_end - 3 * (final_dict[prot_key][2:][c-1][0] - 1) + 1
						p57_gff.write('{}\tblast\texon\t{}\t{}\t.\t-\t.\tParent={}\n'.format(key, ex_end, ex_start, 
							gene_name))
						p57_gff.write('{}\tblast\tintron\t{}\t{}\t.\t-\t.\tParent={};ID=ins{}\n'.format(key, ins_start, 
							ins_end, gene_name, c))
						c += 1
					try:
						ex_end = orf_start
						ex_start = ins_start - 1
						p57_gff.write('{}\tblast\texon\t{}\t{}\t.\t-\t.\tParent={}\n'.format(key, ex_end, ex_start, 
								gene_name))
					except:
						pass

for key in jac_dict.keys():
	orf_start = jac_dict[key][1]
	orf_end = jac_dict[key][2]
	gene_name = jac_dict[key][4].split('.marker')[0]
	if 'c' not in jac_dict[key][3]:
		jac_gff.write('{}\tblast\tCDS\t{}\t{}\t.\t+\t.\tID={}\n'.format(key, jac_dict[key][1], 
			jac_dict[key][2], jac_dict[key][4].split('.marker')[0]))
		for prot_key in final_dict.keys():
			if len(final_dict[prot_key]) == 2:
				pass
			else:
				key_root = re.sub(r'.*(NODE_\d+_length_\d+_cov_\d+.\d+).*', r'\g<1>', prot_key)
				if key_root == key:
					c = 1
					for i in final_dict[prot_key][2:]:
						if i[0] == 1:
							jac_nt.write('>{}_ins{}\n{}\n'.format(prot_key, c, jac_dict[key][0][i[0]-1:3*i[1]-1]))
						else:
							jac_nt.write('>{}_ins{}\n{}\n'.format(prot_key, c, jac_dict[key][0][3*(i[0]-1)-1:3*i[1]-1]))
						if i[0] == i[1]:
							jac_aa.write('>{}_ins{}\n{}\n'.format(prot_key, c, final_dict[prot_key][0][i[0]-1:i[0]]))
						else:
							jac_aa.write('>{}_ins{}\n{}\n'.format(prot_key, c, final_dict[prot_key][0][i[0]-1:i[1]]))
						ins_start = orf_start + 3 * (i[0] - 1)
						ins_end = ins_start + 3 * (i[1] - i[0] + 1) - 1
						if c == 1:
							ex_start = orf_start
							ex_end = orf_start + 3 * (final_dict[prot_key][2:][c-1][0] - 1) - 1
						else:
							ex_start = orf_start + 3 * final_dict[prot_key][2:][c-2][1]
							ex_end = orf_start + 3 * (final_dict[prot_key][2:][c-1][0] - 1) - 1
						jac_gff.write('{}\tblast\texon\t{}\t{}\t.\t+\t.\tParent={}\n'.format(key, ex_start, ex_end, 
							gene_name))
						jac_gff.write('{}\tblast\tintron\t{}\t{}\t.\t+\t.\tParent={};ID=ins{}\n'.format(key, ins_start, 
							ins_end, gene_name, c))
						c += 1
					try:
						ex_start = orf_start + 3 * final_dict[prot_key][-1][1]
						ex_end = orf_end
						jac_gff.write('{}\tblast\texon\t{}\t{}\t.\t+\t.\tParent={}\n'.format(key, ex_start, ex_end, 
							gene_name))
					except:
						pass
	else:
		jac_gff.write('{}\tblast\tCDS\t{}\t{}\t.\t-\t.\tID={}\n'.format(key, jac_dict[key][1], 
			jac_dict[key][2], gene_name))
		for prot_key in final_dict.keys():
			if len(final_dict[prot_key]) == 2:
				pass
			else:
				key_root = re.sub(r'.*(NODE_\d+_length_\d+_cov_\d+.\d+).*', r'\g<1>', prot_key)
				if key_root == key:
					c = 1
					for i in final_dict[prot_key][2:]:
						if i[0] == 1:
							jac_nt.write('>{}_ins{}\n{}\n'.format(prot_key, c, jac_dict[key][0][i[0]-1:3*i[1]]))
						else:
							jac_nt.write('>{}_ins{}\n{}\n'.format(prot_key, c, jac_dict[key][0][3*(i[0]-1):3*i[1]]))
						if i[0] == i[1]:
							jac_aa.write('>{}_ins{}\n{}\n'.format(prot_key, c, final_dict[prot_key][0][i[0]-1:i[0]]))
						else:
							jac_aa.write('>{}_ins{}\n{}\n'.format(prot_key, c, final_dict[prot_key][0][i[0]-1:i[1]]))
						ins_end = orf_end - 3 * (i[0] - 1)
						ins_start = ins_end - 3 * (i[1] - i[0] + 1) + 1
						if c == 1:
							ex_start = orf_end
							ex_end = orf_end - 3 * (final_dict[prot_key][2:][c-1][0] - 1) + 1
						else:
							ex_start = orf_end - 3 * final_dict[prot_key][2:][c-2][1]
							ex_end = orf_end - 3 * (final_dict[prot_key][2:][c-1][0] - 1) + 1
						jac_gff.write('{}\tblast\texon\t{}\t{}\t.\t-\t.\tParent={}\n'.format(key, ex_end, ex_start, 
							gene_name))
						jac_gff.write('{}\tblast\tintron\t{}\t{}\t.\t-\t.\tParent={};ID=ins{}\n'.format(key, ins_start, 
							ins_end, gene_name, c))
						c += 1
					try:
						ex_end = orf_start
						ex_start = ins_start - 1
						jac_gff.write('{}\tblast\texon\t{}\t{}\t.\t-\t.\tParent={}\n'.format(key, ex_end, ex_start, 
								gene_name))
					except:
						pass

p57_aa.close()
p57_nt.close()
p57_gff.close()
p57_errors.close()
jac_aa.close()
jac_nt.close()
jac_gff.close()
jac_errors.close()