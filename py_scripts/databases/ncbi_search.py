#!/usr/bin/python3
from Bio import Entrez
from Bio import SeqIO

Entrez.email = 'zahonova.kristina@gmail.com'

ids = ['AUL74053.1', 'AQP99891.1', 'WP_054554678.1', 'WP_062566226.1', 'WP_036974448.1', 'WP_062569498.1', 'WP_083633683.1', 'WP_105253525.1', 'WP_105189419.1', 'WP_022943569.1', 'WP_023399073.1', 'WP_105199275.1']
# ids = open('/home/kika/MEGAsync/Chlamydomonas/pathways/FASII/cre_acc.txt')

# with open('/home/kika/MEGAsync/Chlamydomonas/pathways/FASII/cre_fabH.txt', 'w') as out:
# 	for prot_id in ids:
# 		print(prot_id)
# 		prot = Entrez.efetch(db='protein', id=prot_id, rettype='gb', retmode='text')
# 		prot_record = SeqIO.read(prot, 'genbank')
# 		# tax = str(prot_record.annotations['taxonomy'][::-1]).replace('\'', '')
# 		# orgn = prot_record.annotations['organism']
# 		out.write('>{} {}\n{}\n'.format(prot_id[:-1], prot_record.description, prot_record.seq))

for prot_id in ids:
	prot = Entrez.efetch(db='protein', id=prot_id, rettype='gb', retmode='text')
	prot_record = SeqIO.read(prot, 'genbank')
	tax = str(prot_record.annotations['taxonomy'][::-1]).replace('\'', '')
	# orgn = prot_record.annotations['organism']
	print(tax)
