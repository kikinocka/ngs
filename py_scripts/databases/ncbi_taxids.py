#!/usr/bin/env python3
import os
from Bio import Entrez
from Bio import SeqIO

Entrez.email = 'kika.zahonova@gmail.com'
Entrez.api_key = 'f1bd64d3d0c99b6455dd3ba822a2e6459a08'

os.chdir('/Users/kika/ownCloud/blasto_comparative/genomes/blobtools/contaminants/')
taxids = ['37003', '655863', '39947', '7048', '2681552', '672011', '1869985', '58919', '7757', '2029752', '4565', '44056', '1286976', '6941', '3055', '67593', '1841481', '280', '2897332', '446860', '879819', '2692235', '9606', '129105', '50954', '65070', '152500', '41117', '57975']

with open('Ovol_cont.taxids.txt', 'w') as out:
	for taxid in taxids:
		try:
			print(taxid)
			search = Entrez.efetch(db='taxonomy', id=taxid, retmode='xml')
			orgn = Entrez.read(search)
			out.write('{}\t{}\n'.format(taxid, orgn[0]['ScientificName']))
		except:
			out.write('{}\tNot found in NCBI taxonomy\n'.format(taxid))
