#!/usr/bin/python3
import os
from Bio import SeqIO
from collections import OrderedDict

os.chdir('/home/kika/paratrypanosoma/')
contamination = open('ncbi_contamination.txt', 'r')
contigs = SeqIO.parse('paratryp_new.fa', 'fasta')
contigs_upd = open('paratryp_new_after_ncbi.fa', 'w')

contamination.readline()
cont = {}
for line in contamination:
	name = line.split('\t')[0]
	start = int(line.split('\t')[1])
	end = int(line.split('\t')[2][:-1])
	if name in cont:
		cont[name].append([start, end])
	else:
		cont[name] = [start, end]

for contig in contigs:
	if contig.description in cont.keys():
		if len(cont[contig.description]) == 3:
			contigs_upd.write('>{}\n{}\n'.format(contig.description, 
				contig.seq[cont[contig.description][1]:cont[contig.description][2][0]-1]))
		elif cont[contig.description][0] == 1:
			contigs_upd.write('>{}\n{}\n'.format(contig.description, 
				contig.seq[cont[contig.description][1]:]))
		elif cont[contig.description][1] == len(contig.seq):
			contigs_upd.write('>{}\n{}\n'.format(contig.description, 
				contig.seq[:cont[contig.description][0]-1]))
		else:
			print(contig.description)
	else:
		contigs_upd.write('>{}\n{}\n'.format(contig.description, contig.seq))