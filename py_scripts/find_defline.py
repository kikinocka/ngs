#!/usr/bin/env python3
import os
from Bio import Entrez, SeqIO
from collections import defaultdict

Entrez.email = 'kika.zahonova@gmail.com'

os.chdir('/storage/brno3-cerit/home/kika/diplonema/oxphos/')
accessions = open('D+E.acc')
blast = open('D+E.dmnd.out')
out = open('D+E.dmnd_hits.defline.tsv', 'w')
errors_def = open('D+E.defline_errors.txt', 'w')
errors_blast = open('D+E.dmnd_errors.txt', 'w')


def defline_assign(acc, errors):
	try:
		sequence = Entrez.efetch(db='protein', id=acc, rettype='gb', retmode='text')
		record = SeqIO.read(sequence, 'genbank')
		defline = record.description
		return defline
	except:
		errors.write('{}\n'.format(acc))
	


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
