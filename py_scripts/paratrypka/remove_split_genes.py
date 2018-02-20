#!/usr/bin/python3
import os
from Bio import SeqIO
from collections import OrderedDict

os.chdir('/home/kika/paratrypanosoma/')
in_gff = open('result_renamed_lengths.gff', 'r')
new_gff = open('result_renamed_lengths_no_split_TEST.gff', 'w')

def get_lengths(gff):
	full_contig = OrderedDict()
	for row in gff:
		if row.startswith('##'):
			full_contig[row.split('\t')[1]] = int(row.split('\t')[3])
		else:
			pass
	return full_contig

full_contig = get_lengths(in_gff)
in_gff.seek(0)

split_genes = []
for row in in_gff:
	if row.startswith('##'):
		new_gff.write(row)
	else:
		for key, value in full_contig.items():
			if row.split('\t')[0] == key:
				if int(row.split('\t')[4]) > value:
					split_genes.append(row.split('\t')[8].split('ID=')[1].split(';')[0])
				else:
					new_gff.write(row)

print(split_genes)
# ['PCON_0034170', 'PCON_0040870', 'PCON_0054950', 'PCON_0072680', 'PCON_0086160']

in_gff.close()
new_gff.close()