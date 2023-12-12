#!/usr/bin/env python3
import os
from Bio import Entrez
from Bio import SeqIO

# get accessions from gi numbers
# https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=281204391&rettype=acc

Entrez.email = 'kika.zahonova@gmail.com'
Entrez.api_key = 'f1bd64d3d0c99b6455dd3ba822a2e6459a08'

os.chdir('/Users/kika/ownCloud/kinetoplastids/kinesins/kinesins/')
acc = open('kin2A.reverse_blast_hsap.acc')

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


with open('kin2A.reverse_blast_hsap.txt', 'w') as out, open('kin2A.reverse_blast_hsap.errors', 'w') as errors:
	for prot_id in ids:
		#get lineage based on accessions
		try:
			print(prot_id)
			prot = Entrez.efetch(db='protein', id=prot_id, rettype='gb', retmode='text')
			prot_record = SeqIO.read(prot, 'genbank')
			# print(prot_record.description)
			# print(prot_record.seq)
			description = prot_record.description
			# tax = prot_record.annotations['taxonomy']
			# tax = str(tax).replace('\'', '').replace('[', '').replace(']', '')#.replace(', ', '_')
			# orgn = str(orgn).replace(' ', '_')
			# full = '{}_{}'.format(tax, orgn)

			# print(orgn)
			# print(description)
			# print(tax)
			# print(tax[0])
			# print(full)

			# out.write('{}\t{}\t{}\n'.format(prot_id, orgn, tax))
			# out.write('{}\t{}\n'.format(prot_id, tax[0]))
			out.write('{}\t{}\n'.format(prot_id, description))
			# out.write('{}\t{}\n'.format(prot_id, full))
			# out.write('>{}\n{}\n'.format(prot_id, prot_id.seq))

			# orgn = prot_record.annotations['organism'].replace(' ', '_')
			# taxid = prot_record.features[0].qualifiers['db_xref'][0].split(':')[1]
			# cds = [x for x in prot_record.features if x.type == 'CDS']
			# for x in cds:
				# gene = x.qualifiers['gene'][0]
				# accession = x.qualifiers['protein_id'][0]
				# translation = x.qualifiers['translation'][0]
				# out.write('>{}__{}__{}__{}\n{}\n'.format(taxid, orgn, gene, accession, translation))	
		except:
			errors.write('{}\n'.format(prot_id))

		# #get GI numbers based on accessions
		# prot = Entrez.efetch(db='protein', id=prot_id, retmode='xml')
		# prot_record = Entrez.read(prot)
		# if prot_record[0]['GBSeq_other-seqids'][-1].startswith('gi'):
		# 	gi = prot_record[0]['GBSeq_other-seqids'][-1].split('|')[1]
		# 	out.write('{}\t{}\n'.format(prot_id, gi))
		# else:
		# 	out.write('{}\t-\n'.format(prot_id))
