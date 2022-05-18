#!/usr/bin/env python3
import os
from Bio import Entrez
from Bio import SeqIO

# get accessions from gi numbers
# https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=281204391&rettype=acc

Entrez.email = 'kika.zahonova@gmail.com'
Entrez.api_key = 'f1bd64d3d0c99b6455dd3ba822a2e6459a08'

os.chdir('/storage/brno3-cerit/home/kika/sl_euglenozoa/v9/V9_DeepSea/')
acc = open('v9.15-99.nt_hits.acc')

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


with open('v9.15-99.nt_hits.lineage', 'w') as out, open('v9.15-99.nt_hits.errors', 'w') as errors:
	for prot_id in ids:
		#get lineage based on accessions
		# try:
			print(prot_id)
			prot = Entrez.efetch(db='nucleotide', id=prot_id, rettype='gb', retmode='text')
			prot_record = SeqIO.read(prot, 'genbank')
			# print(prot_record)
			# tax = prot_record.annotations['taxonomy']
			tax = prot_record.annotations['taxonomy']
			tax = str(tax).replace('\'', '').replace('[', '').replace(']', '')#.replace(', ', '_')
			# orgn = prot_record.annotations['organism']
			# orgn = str(orgn).replace(' ', '_')
			# full = '{}_{}'.format(tax, orgn)
			# print(orgn)
			# print(tax)
			# print(tax[-1:])
			# print(full)
			# out.write('{}\t{}\t{}\n'.format(prot_id, orgn, tax))
			out.write('{}\t{}\n'.format(prot_id, tax))
			# out.write('{}\t{}\n'.format(prot_id, full))
		# except:
		# 	errors.write('{}\n'.format(prot_id))

		# #get GI numbers based on accessions
		# prot = Entrez.efetch(db='protein', id=prot_id, retmode='xml')
		# prot_record = Entrez.read(prot)
		# if prot_record[0]['GBSeq_other-seqids'][-1].startswith('gi'):
		# 	gi = prot_record[0]['GBSeq_other-seqids'][-1].split('|')[1]
		# 	out.write('{}\t{}\n'.format(prot_id, gi))
		# else:
		# 	out.write('{}\t-\n'.format(prot_id))
