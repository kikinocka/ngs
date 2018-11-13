#!/usr/bin/env python3
from re import finditer
from Bio import SeqIO
from Bio.Blast import NCBIXML
from collections import defaultdict

fasta = SeqIO.parse('/home/kika/programs/blast-2.5.0+/bin/p1_scaffolds_k127.fasta', 'fasta')
# nt_out = open('/home/kika/ownCloud/pelomyxa/augustus_training_set/test/p1_mbal_nt.fa', 'w')
# aa_out = open('/home/kika/ownCloud/pelomyxa/augustus_training_set/test/p1_mbal_aa.fa', 'w')
# gff_out = open('/home/kika/ownCloud/pelomyxa/augustus_training_set/test/p1_mbal.gff', 'w')
result_handle = open('/home/kika/ownCloud/pelomyxa/augustus_training_set/test/p1_mbal_blast.xml')
blast_records = NCBIXML.parse(result_handle)

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
		if 'N' in codon:
			aa.append('X')
		else:
			aa.append(gencode[codon])
	return ''.join(aa)

def blast_parser(blast_records):
	intron_dict = defaultdict(list)
	for record in blast_records:
		dashes = [-2]
		try:
			# print(record.alignments[0].accession)
			best = record.alignments[0].hsps[0]
			# print(best.frame[1])
			intron_dict[record.alignments[0].accession].append(best.query)
			intron_dict[record.alignments[0].accession].append(best.frame[1])
			if best.query_start == 1 and best.query_end == record.query_length:
				for match in finditer('-', best.query):
					dashes.append(match.span()[0])
				for i in range(1, len(dashes)):
					if dashes[i] - 1 != dashes[i - 1]:
						intron_start = dashes[i]
					elif i == len(dashes) - 1:
						intron_end = dashes[i]
						coordinates = (intron_start, intron_end)
						intron_dict[record.alignments[0].accession].append(coordinates)
					elif dashes[i] + 1 != dashes[i + 1]:
						intron_end = dashes[i]
						coordinates = (intron_start, intron_end)
						intron_dict[record.alignments[0].accession].append(coordinates)

				# print(best.sbjct_start, best.sbjct_end)

					return intron_dict

		except:
			pass

blast_dict = blast_parser(blast_records)
print(blast_dict)
