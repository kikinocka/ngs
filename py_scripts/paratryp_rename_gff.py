#!/usr/bin/python3
import os
from Bio import SeqIO
from collections import OrderedDict

os.chdir('/home/kika/paratrypanosoma/')
gff = open('result_renamed_after_ncbi.gff', 'r')
without = open('no_.txt', 'r')
out = open('result_renamed_after_ncbi_names_updated.gff', 'w')

no = []
for line in without:
	no.append(line[:-1])

for row in gff:
	seqid = row.split('\t')[0].split('_')[0]
	source = row.split('\t')[1]
	stype = row.split('\t')[2]
	start = int(row.split('\t')[3])
	end = int(row.split('\t')[4])
	score = str(row.split('\t')[5])
	strand = row.split('\t')[6]
	phase = row.split('\t')[7]
	attributes = row.split('\t')[8]
	if seqid in no:
		out.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(seqid, source, stype, start, end, score, strand,
				phase, attributes))
	else:
		out.write(row)
out.close()