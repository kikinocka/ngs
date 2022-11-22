#!/usr/bin/env python3
import os
from Bio import Entrez
from Bio import SeqIO

Entrez.email = 'kika.zahonova@gmail.com'
Entrez.api_key = 'f1bd64d3d0c99b6455dd3ba822a2e6459a08'

os.chdir('/Users/kika/ownCloud/blasto_comparative/genomes/blobtools/Bfru_contaminants/')
taxids = ['6087', '1236908', '727', '96939', '34506', '50023', '291112', '7604', '29139', '665912', '326968', '6279', '35885', 
	'9974', '47314', '2893471', '198719', '176307', '2500532', '34720', '138072', '2895796', '91411', '2689190', '413579', '313723', 
	'486640', '684658', '2692755', '31234', '95602', '6465', '32391', '3735', '2760307', '2587847', '342614', '1077935', '2807096', 
	'1402135', '307643', '717741', '1545044', '1826607', '93060', '2560053', '198431', '43057', '2589076', '2903900', '147645', 
	'929562', '28014', '2067415', '37653', '1580596', '557760', '266', '34004']

with open('Bfru_cont.taxids.txt', 'w') as out, open('Bfru_cont.taxids.errors', 'w') as errors:
	for taxid in taxids:
		try:
			print(taxid)
			search = Entrez.efetch(db='taxonomy', id=taxid, retmode='xml')
			orgn = Entrez.read(search)
			out.write('{}\t{}\n'.format(taxid, orgn[0]['ScientificName']))
		except:
			errors.write('{}\n'.format(taxid))
