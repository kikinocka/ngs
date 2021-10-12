#!/usr/bin/env python3
import os
from Bio import Entrez, SeqIO
from collections import defaultdict

Entrez.email = 'kika.zahonova@gmail.com'

os.chdir('/Users/kika/ownCloud/archamoebae/beta-barrels/')
accessions = open('ena.acc')
blast = open('enan.trinity.NTfilt.dmnd.out')
out = open('ena.blast_hits.defline.tsv', 'w')
errors_def = open('ena.defline_errors.txt', 'w')
errors_blast = open('ena.blast_errors.txt', 'w')


def defline_assign(acc, errors):
	try:
		sequence = Entrez.efetch(db='protein', id=acc, rettype='gb', retmode='text')
		record = SeqIO.read(sequence, 'genbank')
		defline = record.description
	except:
		errors.write('{}\n'.format(acc))
	return defline


blast_dict = {}
for line in blast:
	blast_dict[line.split('\t')[0]] = line.split('\t')[2]

for acc in accessions:
	if acc.strip() in blast_dict:
		print(acc.strip())
		description = defline_assign(blast_dict[acc.strip()], errors_def)
		out.write('{}\t{}\t{}\n'.format(acc.strip(), blast_dict[acc.strip()], description))		
	else:
		errors_blast.write('{}\n'.format(acc.strip()))
