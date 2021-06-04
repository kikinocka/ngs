#!/usr/bin/env python3
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.chdir('/Users/kika/ownCloud/SL_Euglenozoa/V9/')

table = open('otu_table.V9DS.tsv')

tax_dir = {}
for line in table:
	if line.startswith('OTU'):
		pass
	else:
		identity = float(line.split('\t')[21])
		if line.split('\t')[22] == 'No_hit':
			pass
		else:
			taxonomy = line.split('\t')[22].split('|')[1]
			if taxonomy not in tax_dir:
				tax_dir[taxonomy] = [identity]
			else:
				tax_dir[taxonomy].append(identity)
print(tax_dir)


organisms = ['Obazoa', 'Stramenopiles', 'Rhizaria', 'Alveolata', 'Amoebozoa', 'Discoba', 
'Cryptista', 'Archaeplastida', 'Metamonada', 'Haptista', 'Ancyromonadida', 'Protalveolata', 
'Malawimonadidae', 'Mantamonadidea', 'Unknown']


# fig, ax = plt.subplots()
# ax.bar(["0-49", "50-59", "60-69", "70-79", "80-89", "90-100"], iden_list, color='darkgrey')
# plt.xlabel('Similarity to reference sequences [%]')
# plt.ylabel('OTU count')
# # plt.show()
# plt.savefig('OTU_identity.pdf', dpi=300)