#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/SL_Euglenozoa/V9/')
table = open('otu_table.V9DS.no_chimera.2+samples.only_euks.tsv')

with open('otu_table.V9DS.no_chimera.2+samples.only_euks.updated.tsv', 'w') as out:
	for line in table:
		if 'Euglenozoa' in line:
			line = line.replace('Discicristata|Euglenozoa', 'Euglenozoa|Euglenozoa_X')
		elif 'Heterolobosea' in line:
			line = line.replace('Discicristata|Heterolobosea|Heterolobosea_X', 'Heterolobosea|Heterolobosea_X|Heterolobosea_XX')
		elif 'Breviatea' in line:
			line = line.replace('Amoebozoa', 'Obazoa')
		elif 'Pygsuia' in line:
			line = line.replace('Obazoa|Obazoa_X', 'Obazoa|Breviatea')
			line = line.replace('Obazoa_X', 'Breviatea_')
		elif 'Colponemida' in line:
			line = line.replace('Protalveolata', 'Alveolata')
		elif 'Fabomonas' in line or 'Planomonas' in line or 'Nutomonas' in line:
			line = line.replace('Obazoa', 'Ancyromonadida')
		elif 'Picozoa' in line:
			line = line.replace('Cryptista', 'Archaeplastida')
		elif 'Telonemia' in line:
			line = line.replace('Haptista', 'Telonemia')
		elif 'Mantamonas' in line:
			line = line.replace('Eukaryota|Mantamonadidea', 'Eukaryota|CRuMs')
			line = line.replace('Mantamonadidea_X', 'Mantamonadidea')
		elif 'Eukaryota|*' in line:
			line = line.replace('*|*|*|*|*|*|*', 'Eukaryota_X|Eukaryota_XX|Eukaryota_XXX|Eukaryota_XXXX|Eukaryota_XXXXX|Eukaryota_XXXXXX|Eukaryota_XXXXXX_sp')
		elif 'No_hit' in line:
			line = line.replace('No_hit', 'No_hit|No_hit')
		else:
			line = line
		out.write(line)
