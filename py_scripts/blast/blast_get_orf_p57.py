#!/usr/bin/python3
#!!! Check parsing record.query in the blast_parser function (5x) !!!
from Bio import SeqIO
from Bio.Blast import NCBIXML

fasta = SeqIO.parse('/Users/kika/ownCloud/blasto_comparative/genomes/triat_scaffolds.fasta', 'fasta')
nt_out = open('/Users/kika/ownCloud/blasto_comparative/proteins/triat_proteins.fna', 'w')
aa_out = open('/Users/kika/ownCloud/blasto_comparative/proteins/triat_proteins.faa', 'w')
err_out = open('/Users/kika/ownCloud/blasto_comparative/proteins/triat_proteins.errors.txt', 'w')
result_handle = open('/Users/kika/ownCloud/blasto_comparative/proteins/BLASTs/triat.blast_p57proteins.xml')
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
    'TAC':'Y', 'TAT':'Y', 'TAA':'B', 'TAG':'Z',
    'TGC':'C', 'TGT':'C', 'TGA':'J', 'TGG':'W'}

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
	result = {}
	errors = []
	for record in blast_records:
		try:
			best = record.alignments[0]
			min_sstart = False
			max_send = False
			min_qstart = False
			max_qend = False
			frame = best.hsps[0].frame[1]
			if best.hsps[0].expect > 0.01:
				err_out.write('{}:\ttoo high evalue\n'.format(record.query.split(' ')[0]))
			else:
				for hsp in best.hsps:
					if frame == hsp.frame[1]:
						if not min_qstart:
							min_qstart = hsp.query_start
							if frame in [1, 2, 3]:
								min_sstart = best.hsps[0].sbjct_start
							else:
								min_sstart = best.hsps[0].sbjct_end
						if not max_qend:
							max_qend = hsp.query_end
							if frame in [1, 2, 3]:
								max_send = best.hsps[0].sbjct_end
							else:
								max_send = best.hsps[0].sbjct_start
						if min_qstart > hsp.query_start:
							min_qstart = hsp.query_start
							if frame in [1, 2, 3]:
								min_sstart = hsp.sbjct_start
							else:
								min_sstart = hsp.sbjct_end
						if max_qend < hsp.query_end:
							max_qend = hsp.query_end
							if frame in [1, 2, 3]:
								max_send = hsp.sbjct_end
							else:
								max_send = hsp.sbjct_start
					else:
						errors.append(record.query.split(' ')[0])
						if frame in [1, 2, 3]:
							min_sstart = best.hsps[0].sbjct_start
							max_send = best.hsps[0].sbjct_end
						else:
							min_sstart = best.hsps[0].sbjct_end
							max_send = best.hsps[0].sbjct_start
				if frame in [1, 2, 3]:
					result[record.query.split(' ')[0]] = [min_sstart, max_send, frame, best.hit_id,
					record.query_length, min_qstart, max_qend]
				else:
					result[record.query.split(' ')[0]] = [max_send, min_sstart, frame, best.hit_id, 
					record.query_length, min_qstart, max_qend]
		except:
			err_out.write('{}:\tno hit found\n'.format(record.query.split(' ')[0]))
	errors = set(errors)
	for i in errors:
		err_out.write('{}:\thsps frames do not correspond\n'.format(i))
	return result

blast_dict = blast_parser(blast_records)
# print(blast_dict)

for contig in fasta:
	for key, value in blast_dict.items():
		if contig.name == value[3]:
			frame = value[2]
			ref_name = key
			ref_length = value[4]
			ref_start = value[5]-1
			ref_end = value[6]
			ref_dif = ref_length - ref_end
			if frame in [1, 2, 3]:
				print(contig.name + '_____forward')
				seq_start = value[0]-1
				seq_end = value[1]
				if ref_start == 1:
					if translation(contig.seq[seq_start:seq_start+3]) == 'M':
						seq_start = seq_start
					else:
						while translation(contig.seq[seq_start:seq_start+3]) != 'M':
							if seq_start > 2:
								seq_start = seq_start - 3
							else:
								seq_start = seq_start
								break
						else:
							seq_start = seq_start
				else:
					if seq_start > 3*ref_start:
						seq_start = seq_start - 3*ref_start
					else:
						if frame == 1:
							seq_start = 0
						elif frame == 2:
							seq_start = 1
						elif frame == 3:
							seq_start = 2
					while translation(contig.seq[seq_start:seq_start+3]) != 'M':
						if seq_start > 2:
							seq_start = seq_start - 3
						else:
							seq_start = seq_start
							break
					else:
						seq_start = seq_start
				if ref_end == ref_length:
					if translation(contig.seq[seq_end-3:seq_end]) == 'B':
						seq_end = seq_end
					else:
						while translation(contig.seq[seq_end-3:seq_end]) != 'B':
							if seq_end < len(contig.seq) - 3:
								seq_end = seq_end + 3
							else:
								seq_end = seq_end
								break
						else:
							seq_end = seq_end
				else:
					if seq_end + 3*ref_dif < len(contig.seq) - 3:
						seq_end = seq_end + 3*ref_dif
						while translation(contig.seq[seq_end-3:seq_end]) != 'B':
							if seq_end < len(contig.seq) - 3:
								seq_end = seq_end + 3
							else:
								seq_end = seq_end
								break
						else:
							seq_end = seq_end
					else:
						seq_end = len(contig.seq)
				nucleotides = contig.seq[seq_start:seq_end]
				if translation(nucleotides[-3:]) == 'B':
					protein = translation(nucleotides[:-3]).replace('B', 'E').replace('Z', 'E').replace('J', 'W') + '*'
				else:
					protein = translation(nucleotides).replace('B', 'E').replace('Z', 'E').replace('J', 'W')
				nt_out.write('>{} {}\n{}\n'.format(contig.name, ref_name, nucleotides))
				aa_out.write('>{} {}\n{}\n'.format(contig.name, ref_name, protein))
			else:
				print(contig.name + '_____reverse')
				reverse = contig.seq.reverse_complement()
				seq_start = len(reverse) - value[1]
				seq_end = len(reverse) - value[0] + 1
				if ref_start == 1:
					if translation(reverse[seq_start:seq_start+3]) == 'M':
						seq_start = seq_start
					else:
						while translation(reverse[seq_start:seq_start+3]) != 'M':
							if seq_start > 2:
								seq_start = seq_start - 3
							else:
								seq_start = seq_start
								break
						else:
							seq_start = seq_start
				else:
					if seq_start > 3*ref_start:
						seq_start = seq_start - 3*ref_start
					else:
						if frame == 1:
							seq_start = 0
						elif frame == 2:
							seq_start = 1
						elif frame == 3:
							seq_start = 2
					while translation(reverse[seq_start:seq_start+3]) != 'M':
						if seq_start > 2:
							seq_start = seq_start - 3
						else:
							seq_start = seq_start
							break
					else:
						seq_start = seq_start
				if ref_end == ref_length:
					if translation(reverse[seq_end-3:seq_end]) == 'B':
						seq_end = seq_end
					else:
						while translation(reverse[seq_end-3:seq_end]) != 'B':
							if seq_end < len(reverse) - 3:
								seq_end = seq_end + 3
							else:
								seq_end = seq_end
								break
						else:
							seq_end = seq_end
				else:
					if seq_end + 3*ref_dif < len(reverse) - 3:
						seq_end = seq_end + 3*ref_dif
						while translation(reverse[seq_end-3:seq_end]) != 'B':
							if seq_end < len(reverse) - 3:
								seq_end = seq_end + 3
							else:
								seq_end = seq_end
								break
						else:
							seq_end = seq_end
					else:
						seq_end = len(reverse)
				nucleotides = reverse[seq_start:seq_end]
				if translation(nucleotides[-3:]) == 'B':
					protein = translation(nucleotides[:-3]).replace('B', 'E').replace('Z', 'E').replace('J', 'W') + '*'
				else:
					protein = translation(nucleotides).replace('B', 'E').replace('Z', 'E').replace('J', 'W')
				nt_out.write('>{} {}\n{}\n'.format(contig.name, ref_name, nucleotides))
				aa_out.write('>{} {}\n{}\n'.format(contig.name, ref_name, protein))
		else:
			pass

nt_out.close()
aa_out.close()
err_out.close()
