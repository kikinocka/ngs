#!/usr/bin/env python3
#!!! Check parsing record.query.split(' ')[0] in the blast_parser function (6x) !!!
import os
from Bio import SeqIO
from Bio.Blast import NCBIXML

os.chdir('/storage/brno3-cerit/home/kika/elonga_bct_genomes/')
files = [x for x in os.listdir() if x.endswith('.fna')]
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
	'TAC':'Y', 'TAT':'Y', 'TAA':'B', 'TAG':'B',
	'TGC':'C', 'TGT':'C', 'TGA':'B', 'TGG':'W'}

def translation(sequence):
	cut_seq = []
	for i in range(0,len(sequence)-2,3):
		cut_seq.append(sequence[i:i+3])
	aa = []
	for codon in cut_seq:
		if codon not in gencode:
			aa.append('X')
		else:
			aa.append(gencode[codon])
	return ''.join(aa)

def blast_parser(blast_records, file_name):
	result = {}
	errors = []
	for record in blast_records:
		try:
			best = record.alignments[0].hsps[0]
			acc = record.alignments[0].accession
			min_sstart = False
			max_send = False
			min_qstart = False
			max_qend = False
			frame = best.frame[1]
			if best.expect > 0.001:
				err_out.write('{} {}:\ttoo high evalue\n'.format(file_name, record.query))
			else:
				if not min_qstart:
					min_qstart = best.query_start
					if frame in [1, 2, 3]:
						min_sstart = best.sbjct_start
					else:
						min_sstart = best.sbjct_end
				if not max_qend:
					max_qend = best.query_end
					if frame in [1, 2, 3]:
						max_send = best.sbjct_end
					else:
						max_send = best.sbjct_start
				if min_qstart > best.query_start:
					min_qstart = best.query_start
					if frame in [1, 2, 3]:
						min_sstart = best.sbjct_start
					else:
						min_sstart = best.sbjct_end
				if max_qend < best.query_end:
					max_qend = best.query_end
					if frame in [1, 2, 3]:
						max_send = best.sbjct_end
					else:
						max_send = best.sbjct_start
				if frame in [1, 2, 3]:
					result[record.query] = [min_sstart, max_send, frame, acc, 
						record.query_length, min_qstart, max_qend]
				else:
					result[record.query] = [max_send, min_sstart, frame, acc, 
						record.query_length, min_qstart, max_qend]
		except:
			err_out.write('{} {}:\tno hit found\n'.format(file_name, record.query))
	return result

for file in files:
	print(file)
	name = file.split('.fna')[0]
	short_name = 'GCF_' + name.split('_')[1]
	fasta = SeqIO.parse(file, 'fasta')
	nt_out = open('{}_nt.fa'.format(name), 'w')
	aa_out = open('{}_aa.fa'.format(name), 'w')
	err_out = open('{}_errors.txt'.format(name), 'w')
	result_handle = open('{}.tblastn.xml'.format(name))
	blast_records = NCBIXML.parse(result_handle)
	blast_dict = blast_parser(blast_records, short_name)
	# print(blast_dict)

	for contig in fasta:
		for key, value in blast_dict.items():
			if contig.name.split('.')[0] == value[3]:
				frame = value[2]
				ref_name = key.split(' ')[1]
				if frame in [1, 2, 3]:
					print(contig.name + '_____forward')
					seq_start = value[0]-1
					seq_end = value[1]
					prev_stop = seq_start - 3
					while translation(contig.seq[prev_stop:prev_stop+3]) != 'B':
						if prev_stop > 2:
							prev_stop = prev_stop - 3
						else:
							prev_stop = prev_stop
							break
					else:
						prev_stop = prev_stop
					if 'M' not in translation(contig.seq[prev_stop:seq_start-1]):
						if translation(contig.seq[seq_start:seq_start+3]) == 'M':
							new_start = seq_start
						else:
							new_start = prev_stop + 3
					else:
						new_start = prev_stop + 3*translation(contig.seq[prev_stop:seq_start-1]).find('M')
					if translation(contig.seq[seq_end:seq_end+3]) == 'B':
						seq_end = seq_end
					else:
						while translation(contig.seq[seq_end:seq_end+3]) != 'B':
							if seq_end < len(contig.seq) - 3:
								seq_end = seq_end + 3
							else:
								seq_end = seq_end
								break
						else:
							seq_end = seq_end
					nucleotides = contig.seq[new_start:seq_end+3]
					protein = translation(nucleotides)[:-1]
					nt_out.write('>{} {} {}\n{}\n'.format(contig.name, short_name, ref_name, nucleotides))
					aa_out.write('>{} {} {}\n{}\n'.format(contig.name, short_name, ref_name, protein))
				else:
					print(contig.name + '_____reverse')
					reverse = contig.seq.reverse_complement()
					seq_start = len(reverse) - value[1]
					seq_end = len(reverse) - value[0] + 1
					prev_stop = seq_start - 3
					
					while translation(reverse[prev_stop:prev_stop+3]) != 'B':
						if prev_stop > 2:
							prev_stop = prev_stop - 3
						else:
							prev_stop = prev_stop
							break
					else:
						prev_stop = prev_stop
					if 'M' not in translation(reverse[prev_stop:seq_start-1]):
						if translation(reverse[seq_start:seq_start+3]) == 'M':
							new_start = seq_start
						else:
							new_start = prev_stop + 3
					else:
						new_start = prev_stop + 3*translation(reverse[prev_stop:seq_start-1]).find('M')
					if translation(reverse[seq_end:seq_end+3]) == 'B':
						seq_end = seq_end
					else:
						while translation(reverse[seq_end:seq_end+3]) != 'B':
							if seq_end < len(reverse) - 3:
								seq_end = seq_end + 3
							else:
								seq_end = seq_end
								break
						else:
							seq_end = seq_end
					nucleotides = reverse[new_start:seq_end+3]
					protein = translation(nucleotides)[:-1]
					nt_out.write('>{} {} {}\n{}\n'.format(contig.name, short_name, ref_name, nucleotides))
					aa_out.write('>{} {} {}\n{}\n'.format(contig.name, short_name, ref_name, protein))
			else:
				pass

	nt_out.close()
	aa_out.close()
	err_out.close()
