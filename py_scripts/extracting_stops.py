#!/usr/bin/python3
from Bio import SeqIO

out_seqs = open('/home/kika/Dropbox/blasto_project/blastocrithidia/reference_tryps_genomes/Lpyr_GCA_001293395.1_ASM129339v1_CDs_stops_other.fasta', 'w')

infile = SeqIO.parse('/home/kika/Dropbox/blasto_project/blastocrithidia/reference_tryps_genomes/Lpyr_GCA_001293395.1_ASM129339v1_CDs.fasta', 'fasta')
taa = 0
tag = 0
tga = 0
other = 0

for sequence in infile:
	full_seq = sequence.seq
	seq = sequence.seq[-3:]
	name = sequence.name
	if seq == 'taa':
		taa += 1
	elif seq == 'tag':
		tag += 1
	elif seq == 'tga':
		tga += 1
	else:
		other += 1
		out_seqs.write('>{}\n{}\n'.format(name, full_seq))

out_seqs.close()

stops = '{}: {}\n{}: {}\n{}: {}\n{}: {}'.format('taa',taa,'tag',tag,'tga',tga,'other',other)

with open('/home/kika/Dropbox/blasto_project/blastocrithidia/reference_tryps_genomes/Lpyr_GCA_001293395.1_ASM129339v1_CDs_stops.txt', 'w') as result:
	result.write(stops)