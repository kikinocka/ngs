#!/usr/bin/env python3
import os

os.chdir('/storage/brno3-cerit/home/kika/blasto_comparative/blobtools/')

base = 'Bfru'
table = 'reports/{}_tables/phylum.{}.blobDB.table.txt'.format(base, base)
blast = 'blasts/{}.platanus_rnd2_scaffold.l500.gapcloser.nt_1e-20.megablast'.format(base)
cont_table = open('reports/{}_contaminants/{}_contaminants.tsv'.format(base, base), 'w')

for line in open(table):
	if line.startswith('##'):
		pass
	elif 'Euglenozoa' in line:
		pass
	elif 'no-hit' in line:
		pass
	else:
		cont_table.write(line)
