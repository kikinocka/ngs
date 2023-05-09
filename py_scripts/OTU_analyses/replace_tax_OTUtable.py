#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/oil_sands/amplicons/18S-V4-2018/')
table = open('otu_table.no_chimera.tsv')

with open('otu_table.no_chimera.updated.tsv', 'w') as out:
	for line in table:
		if 'Breviatea' in line:
			line = line.replace('Amoebozoa', 'Obazoa')
		elif 'Pygsuia' in line:
			line = line.replace('Obazoa|Obazoa_X', 'Obazoa|Breviatea')
			line = line.replace('Obazoa_X', 'Breviatea_')
		elif 'Colponemida' in line:
			line = line.replace('Protalveolata', 'Alveolata')
		elif 'Fabomonas' in line or 'Planomonas' in line or 'Nutomonas' in line:
			line = line.replace('Obazoa', 'Ancyromonadida')
		elif 'Picozoa' in line:
			line = line.replace('Picozoa', 'Archaeplastida')
		elif 'Telonemia' in line:
			line = line.replace('Haptista', 'Telonemia')
		elif 'Mantamonas' in line:
			line = line.replace('Eukaryota|Mantamonadidea', 'Eukaryota|CRuMs')
			line = line.replace('Mantamonadidea_X', 'Mantamonadidea')
		elif 'Eukaryota|*' in line:
			line = line.replace('*|*|*|*|*|*|*', 'Eukaryota_X|Eukaryota_XX|Eukaryota_XXX|Eukaryota_XXXX|Eukaryota_XXXXX|Eukaryota_XXXXXX|Eukaryota_XXXXXX_sp')
		else:
			line = line
		out.write(line)
