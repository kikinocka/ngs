#!/usr/bin/env python3
from re import finditer
from Bio import SeqIO
from Bio.Blast import NCBIXML
from collections import defaultdict

fasta = SeqIO.parse('/home/kika/programs/blast-2.5.0+/bin/p1_scaffolds_k127.fasta', 'fasta')
nt_out = open('/home/kika/ownCloud/pelomyxa/augustus_training_set/test/p1_mbal_nt.fa', 'w')
aa_out = open('/home/kika/ownCloud/pelomyxa/augustus_training_set/test/p1_mbal_aa.fa', 'w')
# gff_out = open('/home/kika/ownCloud/pelomyxa/augustus_training_set/test/p1_mbal.gff', 'w')
result_handle = open('/home/kika/ownCloud/pelomyxa/augustus_training_set/test/p1_mbal_blast.xml')
blast_records = NCBIXML.parse(result_handle)

def blast_parser(blast_records):
	intron_dict = defaultdict(list)
	try:
		for record in blast_records:
			dashes = [-2]
			best = record.alignments[0].hsps[0]
			if best.frame[1] in [1, 2, 3]:
				sbjct_coord = (best.sbjct_start, best.sbjct_end+3+1)
			else:
				sbjct_coord = (best.sbjct_start-3-1, best.sbjct_end)
			intron_dict[record.alignments[0].accession].append(record.query)
			intron_dict[record.alignments[0].accession].append(best.query)
			intron_dict[record.alignments[0].accession].append(sbjct_coord)
			intron_dict[record.alignments[0].accession].append(best.frame[1])
			if best.expect > 0.01:
				pass
			else:
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
		return intron_dict
	except:
		pass

blast_dict = blast_parser(blast_records)
print(blast_dict)

for contig in fasta:
	for key, value in blast_dict.items():
		if key == contig.name:
			aa_out.write('>{} {} {}\n{}\n'.format(key, value[0], value[4:], value[1]))
			if value[3] in [1, 2, 3]:
				nt_out.write('>{} {} {}\n{}\n'.format(key, value[0], value[4:], contig.seq[value[2][0]:value[2][1]]))
			else:
				nt_out.write('>{} {} {}\n{}\n'.format(key, value[0], value[4:], 
					contig.seq[value[2][0]:value[2][1]].reverse_complement()))