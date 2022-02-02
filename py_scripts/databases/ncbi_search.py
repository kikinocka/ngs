#!/usr/bin/env python3
import os
from Bio import Entrez
from Bio import SeqIO

# get accessions from gi numbers
# https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=281204391&rettype=acc

Entrez.email = 'kika.zahonova@gmail.com'

os.chdir('/Users/kika/ownCloud/oil_sands/metagenomes/20210222_BML-P3S/8-blast-krona/')
acc = open('euk_metaeuk.blast.acc')

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


with open('euk_metaeuk.blast.gi', 'w') as out:
	for prot_id in ids:
		print(prot_id)
		# prot = Entrez.efetch(db='protein', id=prot_id, rettype='gb', retmode='text')
		# prot_record = SeqIO.read(prot, 'genbank')
		# print(prot_record)
		# tax = prot_record.annotations['taxonomy']
		# tax = prot_record.annotations['taxonomy'][::-1]
		# tax = str(tax).replace('\'', '').replace('[', '').replace(']', '')#.replace(', ', '_')
		# orgn = prot_record.annotations['organism']
		# out.write('{}\t{}\t{}\n'.format(prot_id, orgn, tax))
		# print(tax[-1:])
		# out.write('{}\t{}\n'.format(prot_id, tax[-1:]))
		# print(orgn)
		# print(tax)

		#get GI numbers based on accessions
		prot = Entrez.efetch(db='protein', id=prot_id, retmode='xml')
		prot_record = Entrez.read(prot)
		if prot_record[0]['GBSeq_other-seqids'][-1].startswith('gi'):
			gi = prot_record[0]['GBSeq_other-seqids'][-1].split('|')[1]
			out.write('{}\t{}\n'.format(prot_id, gi))
		else:
			out.write('{}\t-\n'.format(prot_id))
