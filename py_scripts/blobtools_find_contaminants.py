#!/usr/bin/env python3
import os

os.chdir('/storage/brno3-cerit/home/kika/blasto_comparative/blobtools/')

base = 'Bfru'
blob_table = open('reports/{0}_tables/phylum.{0}.blobDB.table.txt'.format(base), 'r')
blast = open('blasts/{}.platanus_rnd2_scaffold.l500.gapcloser.nt_1e-20.megablast'.format(base), 'r')
cont_table = open('reports/{0}_contaminants/{0}_contaminants.tsv'.format(base), 'w')
cont_blast_table = open('reports/{0}_contaminants/{0}_contaminants_blast.tsv'.format(base), 'w')

print('Getting contaminants IDs')
contaminants = []
for line in blob_table:
	if line.startswith('##'):
		pass
	elif 'Euglenozoa' in line:
		pass
	elif 'no-hit' in line:
		pass
	else:
		cont_table.write(line)
		contaminants.append(line.split('\t')[0])

print('Getting contaminants BLASTs')
for line in blast:
	for cont in contaminants:
		if cont == line.split('\t')[0]:
			cont_blast_table.write(line)
