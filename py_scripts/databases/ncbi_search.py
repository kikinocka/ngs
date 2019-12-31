#!/usr/bin/env python3
import os
from Bio import Entrez
from Bio import SeqIO

# get accessions from gi numbers
# https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=281204391&rettype=acc

Entrez.email = 'zahonova.kristina@gmail.com'

os.chdir('/home/kika/MEGAsync/diplonema/cardiolipin/CLS_cap/ver3/')
acc = open('cls-cap.acc')

ids = []
for line in acc:
	ids.append(line.strip())

# ids = open('/home/kika/MEGAsync/Chlamydomonas/pathways/FASII/cre_acc.txt')

# with open('/home/kika/MEGAsync/Chlamydomonas/pathways/FASII/cre_fabH.txt', 'w') as out:
# 	for prot_id in ids:
# 		print(prot_id)
# 		prot = Entrez.efetch(db='protein', id=prot_id, rettype='gb', retmode='text')
# 		prot_record = SeqIO.read(prot, 'genbank')
# 		# tax = str(prot_record.annotations['taxonomy'][::-1]).replace('\'', '')
# 		# orgn = prot_record.annotations['organism']
# 		out.write('>{} {}\n{}\n'.format(prot_id[:-1], prot_record.description, prot_record.seq))


with open('cls-cap.lineage', 'w') as out:
	for prot_id in ids:
		print(prot_id)
		prot = Entrez.efetch(db='protein', id=prot_id, rettype='gb', retmode='text')
		prot_record = SeqIO.read(prot, 'genbank')
		tax = prot_record.annotations['taxonomy'][::-1]
		tax = str(tax).replace('\'', '').replace('[', '').replace(']', '').replace(', ', '_')
		orgn = prot_record.annotations['organism']
		out.write('{}\t{} @{}\n'.format(prot_id, orgn, tax))
		# print(orgn)
		# print(tax)
