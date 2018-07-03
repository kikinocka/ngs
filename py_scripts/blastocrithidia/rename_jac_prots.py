#!/usr/bin/python3
import os
from Bio import SeqIO

old = open('/home/kika/MEGAsync/blasto_project/blast_searches/jac_predicted_proteins/jac_transc_prot_best_blast.tsv')
new = open('/home/kika/MEGAsync/blasto_project/blast_searches/jac_predicted_proteins/jac_prot_best_blast.tsv')
os.chdir('/home/kika/MEGAsync/blasto_project/orthofinder/sg_ogs/')
files = os.listdir()

proteins = {}
for line in old:
	protid = line.split('\t')[0].split(' ')[0].replace('jac', 'Jac')
	old_name = line.split('\t')[2]
	proteins[protid] = [old_name]

for line in new:
	protid = line.split('\t')[0].split(' ')[0].replace('jac', 'Jac')
	new_name = line.split('\t')[2]
	if protid in proteins.keys():
		proteins[protid].append(new_name)
	else:
		proteins[protid] = new_name

with open('jac_renamed/data.tsv', 'w') as table:
	table.write('protein\told name\tnew name\n')
	for key, value in proteins.items():
		table.write('{}\t{}\t{}\n'.format(key, value[0], value[1]))

for file in files:
	if file.endswith('.aln'):
		print(file)
		file_name = file.split('.marker')[0]
		new_file = open('jac_renamed/{}_renamed.aln'.format(file_name), 'w')
		sequences = SeqIO.parse(file, 'fasta')
		for seq in sequences:
			if seq.name in proteins.keys():
				desc = seq.description.replace(proteins[seq.name][0], proteins[seq.name][1])
				new_file.write('>{}\n{}\n'.format(desc, seq.seq))
			else:
				new_file.write('>{}\n{}\n'.format(seq.description, seq.seq))