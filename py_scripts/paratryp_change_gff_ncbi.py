#!/usr/bin/python3
import os
from Bio import SeqIO
from collections import OrderedDict

os.chdir('/home/kika/paratrypanosoma/')
in_gff = open('result_renamed.gff', 'r')
contamination = open('ncbi_contamination.txt', 'r')
gff = open('result_renamed_after_ncbi.gff', 'w')

cont = OrderedDict()
for line in contamination:
	name = line.split('\t')[0]
	start = int(line.split('\t')[1])
	end = int(line.split('\t')[2][:-1])
	cont[name] = (start, end)

in_gff.readline()
for row in in_gff:
	seqid = row.split('\t')[0]
	source = row.split('\t')[1]
	stype = row.split('\t')[2]
	start = int(row.split('\t')[3])
	end = int(row.split('\t')[4])
	score = str(row.split('\t')[5])
	strand = row.split('\t')[6]
	phase = row.split('\t')[7]
	attributes = row.split('\t')[8]
	if seqid in cont.keys():
		if int(cont[seqid][0]) == 1:
			start = start - cont[seqid][1]
			end = end - cont[seqid][1]
			gff.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(seqid, source, stype, start, end, score, strand,
				phase, attributes))
		else:
			gff.write(row)
	else:
		gff.write(row)
gff.close()