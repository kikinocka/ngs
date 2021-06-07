#!/usr/bin/env python3
import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir('/Users/kika/ownCloud/SL_Euglenozoa/V9/')

# table = open('otu_table.V9DS.tsv')

# tax_dir = {}
# for line in table:
# 	if line.startswith('OTU'):
# 		pass
# 	else:
# 		identity = float(line.split('\t')[21])
# 		if line.split('\t')[22] == 'No_hit':
# 			pass
# 		else:
# 			taxonomy = line.split('\t')[22].split('|')[1]
# 			if taxonomy not in tax_dir:
# 				tax_dir[taxonomy] = [identity]
# 			else:
# 				tax_dir[taxonomy].append(identity)
# # print(tax_dir)

df = pd.read_csv('V9_deepsea/otu_identities.tsv', sep='\t')
# print(df)

colors = ['#000000', '#CD950B', '#FFB90F', '#FFFF99', '#FAEBD7', 
	'#CAB2D6', '#FB9A99', '#B2DF8A', '#009444', '#C9C9C9', 
	'#1F78B4', '#BCDEB4', '#7FFFD4', '#A6CEE3']

ax = df.plot(x='perc', kind='bar', stacked=True, color=colors, width=0.5, align='center')
ax.set_xticklabels(df.perc, rotation=0)
ax.set_xlabel('Similarity to reference sequences [%]')
ax.set_ylabel('OTU count')
ax.yaxis.grid(True, which='major', linestyle='-', linewidth=0.25)
ax.set_axisbelow(True)
ax.legend(bbox_to_anchor=(1, 1), frameon=False)
plt.tight_layout()
# plt.show()
plt.savefig('V9_deepsea/otu_identities.pdf', dpi=300)
