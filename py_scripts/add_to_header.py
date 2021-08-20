#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/data/eukprot/')
eukprot = SeqIO.parse('eukprot_v2_proteins_renamed.faa', 'fasta')
table = open('EukProt_included_data_sets.v02.taxids.tsv')

taxids = {}
for line in table:
	eukid = line.split('\t')[0]
	taxid = line.split('\t')[1]
	taxids[eukid] = taxid

# |kraken:taxid|XXX
with open('eukprot_v2_proteins_renamed.taxids.faa', 'w') as update:
	for seq in eukprot:
		eukid = seq.name.split('_')[0]
		update.write('>{}|kraken:taxid|{}\n{}\n'.format(seq.name, taxids[eukid], seq.seq))
