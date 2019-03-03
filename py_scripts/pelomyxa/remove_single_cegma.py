#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/home/kika/ownCloud/pelomyxa/genome_assembly/cegma/clean_ht2_p-rna-scaffolder/')
gff = open('pelo_p-rna-scaffolder.cegma.gff')
gff_upd = open('pelo_final.cegma_upd.gff', 'w')

for line in gff:
	if line.split('\t')[2] == 'Single':
		pass
	else:
		gff_upd.write(line)

gff_upd.close()
