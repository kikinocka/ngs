#!/usr/bin/python3
from Bio import SeqIO
import re

nucl_file = SeqIO.parse('/home/kika/Dropbox/blastocrithidia/genome/assembly/p57_DNA_scaffolds.fa', 'fasta')
prot_file = SeqIO.parse('/home/kika/Dropbox/blastocrithidia/genes/insertions/alignments/out_p57.fasta', 'fasta')
outfile = open('/home/kika/scripts/out_p57_nt.fasta', 'w')
err = open('/home/kika/scripts/out_errors_nt.fa', 'w')

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
	'TAC':'Y', 'TAT':'Y', 'TAA':'X', 'TAG':'X',
	'TGC':'C', 'TGT':'C', 'TGA':'X', 'TGG':'W'}

def translation(seq):
	cut_seq = []
	for i in range(0,len(seq)-2,3):
		cut_seq.append(seq[i:i+3])
	aa = []
	for codon in cut_seq:
		if 'N' in codon:
			aa.append('X')
		else:
			aa.append(gencode[codon])
	return ''.join(aa)

nucleotides = {}
proteins = {}

for sequence in nucl_file:
	nucleotides[sequence.name] = sequence.seq

for sequence in prot_file:
	proteins[sequence.name] = sequence.seq

for key in proteins.keys():
	key_root = re.sub('_\d+\Z', '', key)
	print(key_root)
	if key_root in nucleotides.keys():
		nucl = nucleotides[key_root]
		reverse = nucl.reverse_complement()
		prot = proteins[key]
		if str(prot) in translation(nucl):
			start = (translation(nucl).find(str(prot))) * 3
			end = start + (len(prot) * 3)
			frame = 1
			if len(nucl[start:end]) <= 6:
				pass
			else:
				outfile.write('>{}_f{}\n{}\n'.format(key, frame, nucl[start:end]))
		elif str(proteins[key]) in translation(nucl[1:]):
			start = (translation(nucl[1:]).find(str(prot))) * 3
			end = start + (len(prot) * 3)
			frame = 2
			if len(nucl[start:end]) <= 6:
				pass
			else:
				outfile.write('>{}_f{}\n{}\n'.format(key, frame, nucl[start:end]))
		elif str(proteins[key]) in translation(nucl[2:]):
			start = (translation(nucl[2:]).find(str(prot))) * 3
			end = start + (len(prot) * 3)
			frame = 3
			if len(nucl[start:end]) <= 6:
				pass
			else:
				outfile.write('>{}_f{}\n{}\n'.format(key, frame, nucl[start:end]))
		elif str(proteins[key]) in translation(reverse):
			start = (translation(reverse).find(str(prot))) * 3
			end = start + (len(prot) * 3)
			frame = 4
			if len(reverse[start:end]) <= 6:
				pass
			else:
				outfile.write('>{}_f{}\n{}\n'.format(key, frame, reverse[start:end]))
		elif str(proteins[key]) in translation(reverse[1:]):
			start = (translation(reverse[1:]).find(str(prot))) * 3
			end = start + (len(prot) * 3)
			frame = 5
			if len(reverse[start:end]) <= 6:
				pass
			else:
				outfile.write('>{}_f{}\n{}\n'.format(key, frame, reverse[start:end]))
		elif str(proteins[key]) in translation(reverse[2:]):
			start = (translation(reverse[2:]).find(str(prot))) * 3
			end = start + (len(prot) * 3)
			frame = 6
			if len(reverse[start:end]) <= 6:
				pass
			else:
				outfile.write('>{}_f{}\n{}\n'.format(key, frame, reverse[start:end]))
		else:
			err.write('{}: {}\n'.format(key, 'no ORF found'))

outfile.close()