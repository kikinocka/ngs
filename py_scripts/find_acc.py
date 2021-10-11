#!/usr/bin/env python3
import os
from Bio import Entrez, SeqIO
from collections import defaultdict

Entrez.email = 'kika.zahonova@gmail.com'

os.chdir('/mnt/mokosz/home/kika/beta-barrels/')
accessions = open('ena.acc')
blast = open('enan.trinity.NTfilt.dmnd.out')
out = open('ena.blast_hits.defline.tsv', 'w')
errors = open('ena.defline_errors.txt', 'w')


def defline_assign(acc, database, errors):
	try:
		sequence = Entrez.efetch(db=database, id=acc, rettype='gb', retmode='text')
		record = SeqIO.read(sequence, 'genbank')
	except:
		errors.write('{}\n'.format(acc))
	return record.description


blast_dict = {}
for line in blast:
	blast_dict[line.split('\t')[0]] = line.split('\t')[2]

for acc in accessions:
	if acc.strip() in blast_dict:
		description = defline_assign(acc.strip(), 'protein', errors)
		out.write('{}\t{}\t\n'.format(acc.strip(), blast_dict[acc.strip()], description))		
	else:
		errors.write('{}\n'.format(acc.strip()))
