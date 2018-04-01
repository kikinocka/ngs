#!/usr/bin/python3
from Bio import Entrez
from Bio import SeqIO

Entrez.email = 'zahonova.kristina@gmail.com'

# ids = ['XP_001701303', 'XP_001702319', 'XP_001703187', 'XP_001696945', 'XP_001700442']
ids = open('/home/kika/MEGAsync/Chlamydomonas/pathways/FASII/cre_acc.txt')

with open('/home/kika/MEGAsync/Chlamydomonas/pathways/FASII/cre_fabH.txt', 'w') as out:
	for prot_id in ids:
		print(prot_id)
		prot = Entrez.efetch(db='protein', id=prot_id, rettype='gb', retmode='text')
		prot_record = SeqIO.read(prot, 'genbank')
		# tax = str(prot_record.annotations['taxonomy'][::-1]).replace('\'', '')
		# orgn = prot_record.annotations['organism']
		out.write('>{} {}\n{}\n'.format(prot_id[:-1], prot_record.description, prot_record.seq))