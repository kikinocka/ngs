#!/usr/bin/python3
import os
import re
from Bio import SeqIO, AlignIO
from collections import defaultdict

p57_genome = '/media/4TB1/blastocrithidia/genome_assembly/p57_scaffolds.fa'
jac_genome = '/media/4TB1/blastocrithidia/genome_assembly/jaculum_scaffolds.fa'
triat_transc = '/media/4TB1/blastocrithidia/transcriptome_assembly/trinity_denovo/triat_trinity.fasta'
bexlh_transc = '/media/4TB1/blastocrithidia/transcriptome_assembly/trinity_denovo/blobtools/lhes1/bexlh1_strict.fa'

os.chdir('/media/4TB1/blastocrithidia/orthofinder/sg_ogs/alignments/jac_renamed/')
files = os.listdir()
no_orf = open('no_orf.txt', 'w')
not_genome = open('not_genome.txt', 'w')
p57_gff = open('p57_insertions.gff', 'w')
jac_gff = open('jac_insertions.gff', 'w')
triat_gff = open('triat_insertions.gff', 'w')
bexlh_gff = open('bexlh_insertions.gff', 'w')

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
			aln_pos_list = [-2]
			for position, value in sample.items():
				if value == 1:
					aln_pos_list.append(position)
					position_list.append(position - seq_seq[:position].count('-'))
			start = -1
			aln_start = -1
			for position in range(1,len(position_list)):
				if position_list[position] - 1 != position_list[position - 1]:
					start = int(position_list[position])
					aln_start = int(aln_pos_list[position])
				if position == len(position_list) - 1:
					stop = int(position_list[position])
					aln_stop = int(aln_pos_list[position])
					coordinates = (start, stop, aln_start, aln_stop)
					result_dict[seq_name].append(coordinates)
				elif position_list[position] + 1 != position_list[position + 1]:
					stop = int(position_list[position])
					aln_stop = int(aln_pos_list[position])
					coordinates = (start, stop, aln_start, aln_stop)
					result_dict[seq_name].append(coordinates)
		p57_triat_BexLH_jac += 1
	return result_dict
	#prot_name : [prot_seq, file_name, (start,stop, aln_start,aln_stop), (start,stop, aln_start,aln_stop)]
	#									     	ins1		   					ins2

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

def orf_genome(species, result_dict, genome):
	contigs = SeqIO.parse(genome, 'fasta')
	proteins_from_aln = result_dict
	sp_contigs = {}
	for contig in contigs:
		sp_contigs[contig.name] = contig.seq
	orf = {}
	not_genome_dict = {}
	no_orf_dict = {}
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
					orf[proteins_from_aln[key][1]] = [key, nucl[orf_start-1:orf_end], orf_start, orf_end, 
						frame]
				elif str(prot) in translation(nucl[1:]):
					orf_start = 3 * (translation(nucl[1:]).find(str(prot))) + 2
					orf_end = orf_start + (3 * len(prot)) + 2
					frame = '2'
					orf[proteins_from_aln[key][1]] = [key, nucl[orf_start-1:orf_end], orf_start, orf_end, 
						frame]
				elif str(prot) in translation(nucl[2:]):
					orf_start = 3 * (translation(nucl[2:]).find(str(prot))) + 3
					orf_end = orf_start + (3 * len(prot)) + 2
					frame = '3'
					orf[proteins_from_aln[key][1]] = [key, nucl[orf_start-1:orf_end], orf_start, orf_end, 
						frame]
				elif str(prot) in translation(reverse):
					orf_start = 3 * (translation(reverse).find(str(prot)))
					orf_end = orf_start + (3 * len(prot)) + 3
					orf_start_contig = len(reverse) - orf_end + 1
					orf_end_contig = len(reverse) - orf_start
					frame = 'c1'
					orf[proteins_from_aln[key][1]] = [key, reverse[orf_start:orf_end], orf_start_contig, 
						orf_end_contig, frame]
				elif str(prot) in translation(reverse[1:]):
					orf_start = 3 * (translation(reverse[1:]).find(str(prot))) + 1
					orf_end = orf_start + (3 * len(prot)) + 3
					orf_start_contig = len(reverse) - orf_end + 1
					orf_end_contig = len(reverse) - orf_start
					frame = 'c2'
					orf[proteins_from_aln[key][1]] = [key, reverse[orf_start:orf_end], orf_start_contig, 
						orf_end_contig, frame]
				elif str(prot) in translation(reverse[2:]):
					orf_start = 3 * (translation(reverse[2:]).find(str(prot))) + 2
					orf_end = orf_start + (3 * len(prot)) + 3
					orf_start_contig = len(reverse) - orf_end + 1
					orf_end_contig = len(reverse) - orf_start
					frame = 'c3'
					orf[proteins_from_aln[key][1]] = [key, reverse[orf_start:orf_end], orf_start_contig, 
						orf_end_contig, frame]
				else:
					no_orf_dict[key] = proteins_from_aln[key][1]
			else:
				not_genome_dict[key] = proteins_from_aln[key][1]
	return orf, no_orf_dict, not_genome_dict
	#orf
	#file name : [prot_name		orf sequence 	orf start 	orf end 	frame]
	#			   [0]				[1]			[2]			[3]			[4]	

def orf_transcriptome(species, result_dict, transcriptome):
	contigs = SeqIO.parse(transcriptome, 'fasta')
	proteins_from_aln = result_dict
	sp_contigs = {}
	for contig in contigs:
		sp_contigs[contig.name] = contig.seq
	orf = {}
	not_genome_dict = {}
	no_orf_dict = {}
	for key in proteins_from_aln.keys():
		if species in key:
			key_root = re.sub(r'.*(TRINITY_\w+_\w\d_\w\d_\w\d).*', r'\g<1>', key)
			if key_root in sp_contigs.keys():
				nucl = sp_contigs[key_root]
				reverse = nucl.reverse_complement()
				prot = proteins_from_aln[key][0]
				if str(prot) in translation(nucl):
					orf_start = 3 * (translation(nucl).find(str(prot))) + 1
					orf_end = orf_start + (3 * len(prot)) + 2
					frame = '1'
					orf[proteins_from_aln[key][1]] = [key, nucl[orf_start-1:orf_end], orf_start, orf_end, 
						frame]
				elif str(prot) in translation(nucl[1:]):
					orf_start = 3 * (translation(nucl[1:]).find(str(prot))) + 2
					orf_end = orf_start + (3 * len(prot)) + 2
					frame = '2'
					orf[proteins_from_aln[key][1]] = [key, nucl[orf_start-1:orf_end], orf_start, orf_end, 
						frame]
				elif str(prot) in translation(nucl[2:]):
					orf_start = 3 * (translation(nucl[2:]).find(str(prot))) + 3
					orf_end = orf_start + (3 * len(prot)) + 2
					frame = '3'
					orf[proteins_from_aln[key][1]] = [key, nucl[orf_start-1:orf_end], orf_start, orf_end,
						frame]
				elif str(prot) in translation(reverse):
					orf_start = 3 * (translation(reverse).find(str(prot)))
					orf_end = orf_start + (3 * len(prot)) + 3
					orf_start_contig = len(reverse) - orf_end + 1
					orf_end_contig = len(reverse) - orf_start
					frame = 'c1'
					orf[proteins_from_aln[key][1]] = [key, reverse[orf_start:orf_end], orf_start_contig, 
						orf_end_contig, frame]
				elif str(prot) in translation(reverse[1:]):
					orf_start = 3 * (translation(reverse[1:]).find(str(prot))) + 1
					orf_end = orf_start + (3 * len(prot)) + 3
					orf_start_contig = len(reverse) - orf_end + 1
					orf_end_contig = len(reverse) - orf_start
					frame = 'c2'
					orf[proteins_from_aln[key][1]] = [key, reverse[orf_start:orf_end], orf_start_contig, 
						orf_end_contig, frame]
				elif str(prot) in translation(reverse[2:]):
					orf_start = 3 * (translation(reverse[2:]).find(str(prot))) + 2
					orf_end = orf_start + (3 * len(prot)) + 3
					orf_start_contig = len(reverse) - orf_end + 1
					orf_end_contig = len(reverse) - orf_start
					frame = 'c3'
					orf[proteins_from_aln[key][1]] = [key, reverse[orf_start:orf_end], orf_start_contig, 
						orf_end_contig, frame]
				else:
					no_orf_dict[key] = proteins_from_aln[key][1]
			else:
				not_genome_dict[key] = proteins_from_aln[key][1]
	return orf, no_orf_dict, not_genome_dict
	#orf
	#file name : [prot_name		orf sequence 	orf start 	orf end 	frame]
	#			   [0]				[1]			[2]			[3]			[4]	

print('Gathering insertions from alignments')
final_dict = {}
for file in files:
	if file.endswith('.aln'):
		print(file)
		ins_aln_positions = find_insertion(file)
		result_dict = get_peptides(ins_aln_positions, file)
		final_dict.update(result_dict)

		p57_dict, no_orf_dict, not_genome_dict = orf_genome('Bp57', final_dict, p57_genome)

		jac_dict = orf_genome('Jac', final_dict, jac_genome)[0]
		no_orf_dict.update(orf_genome('Jac', final_dict, jac_genome)[1])
		not_genome_dict.update(orf_genome('Jac', final_dict, jac_genome)[2])

		triat_dict = orf_transcriptome('Btri', final_dict, triat_transc)[0]
		no_orf_dict.update(orf_transcriptome('Btri', final_dict, triat_transc)[1])
		not_genome_dict.update(orf_transcriptome('Btri', final_dict, triat_transc)[2])

		bexlh_dict = orf_transcriptome('Bexl', final_dict, bexlh_transc)[0]
		no_orf_dict.update(orf_transcriptome('Bexl', final_dict, bexlh_transc)[1])
		not_genome_dict.update(orf_transcriptome('Bexl', final_dict, bexlh_transc)[2])

print('Writting errors to files')
for key, value in no_orf_dict.items():
	no_orf.write('{}\t{}\n'.format(value, key))
for key, value in not_genome_dict.items():
	not_genome.write('{}\t{}\n'.format(value, key))

#final_dict
#prot_name : [prot_seq, file_name, (start,stop, aln_start,aln_stop), (start,stop, aln_start,aln_stop)]
#									     	ins1		   					ins2
#sp_dict
#file name : [prot_name		orf sequence 	orf start 	orf end 	frame]
#			   [0]				[1]			[2]			[3]			[4]	

print('Writting insertions found in Bp57 proteins to files')
for key, value in p57_dict.items():
	og = key.split('_')[0]
	contig = value[0].split(' ')[2]
	orf_start = value[2]
	orf_end = value[3]
	frame = value[4]
	if 'c' not in frame:
		p57_gff.write('{}\tblast\tCDS\t{}\t{}\t.\t+\t.\tID={}\n'.format(contig, orf_start, orf_end, og))
		for prot_key, prot_value in final_dict.items():
			if value[0] == prot_key:
				if len(prot_value) == 2:
					pass
				else:
					p57_gff.write('{}\tblast\texon\t{}\t{}\t.\t+\t.\tParent={}\n'.format(contig, orf_start, 
						orf_start + 3*prot_value[2][0] - 4, og))
					for i in range(len(prot_value[2:])):
						p57_gff.write('{}\tblast\tintron\t{}\t{}\t.\t+\t.\tParent={};ID=ins{}_{}-{}\n'.format(
								contig, orf_start + 3*prot_value[2:][i][0] - 3, 
								orf_start + 3*prot_value[2:][i][1] - 1, og, i+1, prot_value[2:][i][2],
								prot_value[2:][i][3]))
						if i+1 == len(prot_value[2:]):
							pass
						else:
							p57_gff.write('{}\tblast\texon\t{}\t{}\t.\t+\t.\tParent={}\n'.format(contig, 
								orf_start + 3*prot_value[2:][i][1], orf_start + 3*prot_value[2:][i+1][0] - 4, og))
						i += 1
					p57_gff.write('{}\tblast\texon\t{}\t{}\t.\t+\t.\tParent={}\n'.format(contig, 
						orf_start + 3*prot_value[-1][1], orf_end, og))
	else:
		p57_gff.write('{}\tblast\tCDS\t{}\t{}\t.\t-\t.\tID={}\n'.format(contig, orf_start, orf_end, og))
		for prot_key, prot_value in final_dict.items():
			if value[0] in prot_key:
				if len(prot_value) == 2:
					pass
				else:
					p57_gff.write('{}\tblast\texon\t{}\t{}\t.\t-\t.\tParent={}\n'.format(contig,  
						orf_end - 3*prot_value[2][0] + 1 + 3, orf_end, og))
					for i in range(len(prot_value[2:])):
						p57_gff.write('{}\tblast\tintron\t{}\t{}\t.\t-\t.\tParent={};ID=ins{}_{}-{}\n'.format(
								contig, orf_end - 3*prot_value[2:][i][1] + 1, 
								orf_end - 3*prot_value[2:][i][0] + 1 + 2, og, i+1, prot_value[2:][i][2],
								prot_value[2:][i][3]))
						if i+1 == len(prot_value[2:]):
							pass
						else:
							p57_gff.write('{}\tblast\texon\t{}\t{}\t.\t-\t.\tParent={}\n'.format(contig,
								orf_end - 3*prot_value[2:][i+1][0] + 1 + 3, orf_end - 3*prot_value[2:][i][1], og))
						i += 1
					p57_gff.write('{}\tblast\texon\t{}\t{}\t.\t-\t.\tParent={}\n'.format(contig, orf_start, 
						 orf_end - 3*prot_value[-1][1], og))

print('Writting insertions found in Jac proteins to files')
for key, value in jac_dict.items():
	og = key.split('_')[0]
	contig = value[0].split(' ')[2]
	orf_start = value[2]
	orf_end = value[3]
	frame = value[4]
	if 'c' not in frame:
		jac_gff.write('{}\tblast\tCDS\t{}\t{}\t.\t+\t.\tID={}\n'.format(contig, orf_start, orf_end, og))
		for prot_key, prot_value in final_dict.items():
			if value[0] == prot_key:
				if len(prot_value) == 2:
					pass
				else:
					jac_gff.write('{}\tblast\texon\t{}\t{}\t.\t+\t.\tParent={}\n'.format(contig, orf_start, 
						orf_start + 3*prot_value[2][0] - 4, og))
					for i in range(len(prot_value[2:])):
						jac_gff.write('{}\tblast\tintron\t{}\t{}\t.\t+\t.\tParent={};ID=ins{}_{}-{}\n'.format(
								contig, orf_start + 3*prot_value[2:][i][0] - 3, 
								orf_start + 3*prot_value[2:][i][1] - 1, og, i+1, prot_value[2:][i][2],
								prot_value[2:][i][3]))
						if i+1 == len(prot_value[2:]):
							pass
						else:
							jac_gff.write('{}\tblast\texon\t{}\t{}\t.\t+\t.\tParent={}\n'.format(contig, 
								orf_start + 3*prot_value[2:][i][1], orf_start + 3*prot_value[2:][i+1][0] - 4, og))
						i += 1
					jac_gff.write('{}\tblast\texon\t{}\t{}\t.\t+\t.\tParent={}\n'.format(contig, 
						orf_start + 3*prot_value[-1][1], orf_end, og))
	else:
		jac_gff.write('{}\tblast\tCDS\t{}\t{}\t.\t-\t.\tID={}\n'.format(contig, orf_start, orf_end, og))
		for prot_key, prot_value in final_dict.items():
			if value[0] in prot_key:
				if len(prot_value) == 2:
					pass
				else:
					jac_gff.write('{}\tblast\texon\t{}\t{}\t.\t-\t.\tParent={}\n'.format(contig,  
						orf_end - 3*prot_value[2][0] + 1 + 3, orf_end, og))
					for i in range(len(prot_value[2:])):
						jac_gff.write('{}\tblast\tintron\t{}\t{}\t.\t-\t.\tParent={};ID=ins{}_{}-{}\n'.format(
								contig, orf_end - 3*prot_value[2:][i][1] + 1, 
								orf_end - 3*prot_value[2:][i][0] + 1 + 2, og, i+1, prot_value[2:][i][2],
								prot_value[2:][i][3]))
						if i+1 == len(prot_value[2:]):
							pass
						else:
							jac_gff.write('{}\tblast\texon\t{}\t{}\t.\t-\t.\tParent={}\n'.format(contig,
								orf_end - 3*prot_value[2:][i+1][0] + 1 + 3, orf_end - 3*prot_value[2:][i][1], og))
						i += 1
					jac_gff.write('{}\tblast\texon\t{}\t{}\t.\t-\t.\tParent={}\n'.format(contig, orf_start, 
						 orf_end - 3*prot_value[-1][1], og))

print('Writting insertions found in Btri proteins to files')
for key, value in triat_dict.items():
	og = key.split('_')[0]
	contig = value[0].split(' ')[2]
	orf_start = value[2]
	orf_end = value[3]
	frame = value[4]
	if 'c' not in frame:
		triat_gff.write('{}\tblast\tCDS\t{}\t{}\t.\t+\t.\tID={}\n'.format(contig, orf_start, orf_end, og))
		for prot_key, prot_value in final_dict.items():
			if value[0] == prot_key:
				if len(prot_value) == 2:
					pass
				else:
					triat_gff.write('{}\tblast\texon\t{}\t{}\t.\t+\t.\tParent={}\n'.format(contig, orf_start, 
						orf_start + 3*prot_value[2][0] - 4, og))
					for i in range(len(prot_value[2:])):
						triat_gff.write('{}\tblast\tintron\t{}\t{}\t.\t+\t.\tParent={};ID=ins{}_{}-{}\n'.format(
								contig, orf_start + 3*prot_value[2:][i][0] - 3, 
								orf_start + 3*prot_value[2:][i][1] - 1, og, i+1, prot_value[2:][i][2],
								prot_value[2:][i][3]))
						if i+1 == len(prot_value[2:]):
							pass
						else:
							triat_gff.write('{}\tblast\texon\t{}\t{}\t.\t+\t.\tParent={}\n'.format(contig, 
								orf_start + 3*prot_value[2:][i][1], orf_start + 3*prot_value[2:][i+1][0] - 4, og))
						i += 1
					triat_gff.write('{}\tblast\texon\t{}\t{}\t.\t+\t.\tParent={}\n'.format(contig, 
						orf_start + 3*prot_value[-1][1], orf_end, og))
	else:
		triat_gff.write('{}\tblast\tCDS\t{}\t{}\t.\t-\t.\tID={}\n'.format(contig, orf_start, orf_end, og))
		for prot_key, prot_value in final_dict.items():
			if value[0] in prot_key:
				if len(prot_value) == 2:
					pass
				else:
					triat_gff.write('{}\tblast\texon\t{}\t{}\t.\t-\t.\tParent={}\n'.format(contig,  
						orf_end - 3*prot_value[2][0] + 1 + 3, orf_end, og))
					for i in range(len(prot_value[2:])):
						triat_gff.write('{}\tblast\tintron\t{}\t{}\t.\t-\t.\tParent={};ID=ins{}_{}-{}\n'.format(
								contig, orf_end - 3*prot_value[2:][i][1] + 1, 
								orf_end - 3*prot_value[2:][i][0] + 1 + 2, og, i+1, prot_value[2:][i][2],
								prot_value[2:][i][3]))
						if i+1 == len(prot_value[2:]):
							pass
						else:
							triat_gff.write('{}\tblast\texon\t{}\t{}\t.\t-\t.\tParent={}\n'.format(contig,
								orf_end - 3*prot_value[2:][i+1][0] + 1 + 3, orf_end - 3*prot_value[2:][i][1], og))
						i += 1
					triat_gff.write('{}\tblast\texon\t{}\t{}\t.\t-\t.\tParent={}\n'.format(contig, orf_start, 
						 orf_end - 3*prot_value[-1][1], og))

print('Writting insertions found in Bexl proteins to files')
for key, value in bexlh_dict.items():
	og = key.split('_')[0]
	contig = value[0].split(' ')[2]
	orf_start = value[2]
	orf_end = value[3]
	frame = value[4]
	if 'c' not in frame:
		bexlh_gff.write('{}\tblast\tCDS\t{}\t{}\t.\t+\t.\tID={}\n'.format(contig, orf_start, orf_end, og))
		for prot_key, prot_value in final_dict.items():
			if value[0] == prot_key:
				if len(prot_value) == 2:
					pass
				else:
					bexlh_gff.write('{}\tblast\texon\t{}\t{}\t.\t+\t.\tParent={}\n'.format(contig, orf_start, 
						orf_start + 3*prot_value[2][0] - 4, og))
					for i in range(len(prot_value[2:])):
						bexlh_gff.write('{}\tblast\tintron\t{}\t{}\t.\t+\t.\tParent={};ID=ins{}_{}-{}\n'.format(
								contig, orf_start + 3*prot_value[2:][i][0] - 3, 
								orf_start + 3*prot_value[2:][i][1] - 1, og, i+1, prot_value[2:][i][2],
								prot_value[2:][i][3]))
						if i+1 == len(prot_value[2:]):
							pass
						else:
							bexlh_gff.write('{}\tblast\texon\t{}\t{}\t.\t+\t.\tParent={}\n'.format(contig, 
								orf_start + 3*prot_value[2:][i][1], orf_start + 3*prot_value[2:][i+1][0] - 4, og))
						i += 1
					bexlh_gff.write('{}\tblast\texon\t{}\t{}\t.\t+\t.\tParent={}\n'.format(contig, 
						orf_start + 3*prot_value[-1][1], orf_end, og))
	else:
		bexlh_gff.write('{}\tblast\tCDS\t{}\t{}\t.\t-\t.\tID={}\n'.format(contig, orf_start, orf_end, og))
		for prot_key, prot_value in final_dict.items():
			if value[0] in prot_key:
				if len(prot_value) == 2:
					pass
				else:
					bexlh_gff.write('{}\tblast\texon\t{}\t{}\t.\t-\t.\tParent={}\n'.format(contig,  
						orf_end - 3*prot_value[2][0] + 1 + 3, orf_end, og))
					for i in range(len(prot_value[2:])):
						bexlh_gff.write('{}\tblast\tintron\t{}\t{}\t.\t-\t.\tParent={};ID=ins{}_{}-{}\n'.format(
								contig, orf_end - 3*prot_value[2:][i][1] + 1, 
								orf_end - 3*prot_value[2:][i][0] + 1 + 2, og, i+1, prot_value[2:][i][2],
								prot_value[2:][i][3]))
						if i+1 == len(prot_value[2:]):
							pass
						else:
							bexlh_gff.write('{}\tblast\texon\t{}\t{}\t.\t-\t.\tParent={}\n'.format(contig,
								orf_end - 3*prot_value[2:][i+1][0] + 1 + 3, orf_end - 3*prot_value[2:][i][1], og))
						i += 1
					bexlh_gff.write('{}\tblast\texon\t{}\t{}\t.\t-\t.\tParent={}\n'.format(contig, orf_start, 
						 orf_end - 3*prot_value[-1][1], og))

no_orf.close()
not_genome.close()
p57_gff.close()
jac_gff.close()
triat_gff.close()
bexlh_gff.close()