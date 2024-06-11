#!/usr/bin/env python3
import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir('/Users/kika/ownCloud/SL_Euglenozoa/V9/supergroups/')
# out_perc = open('Rhizaria.tsv', 'w')

# #several OTU tables
# v9 = pd.read_csv('V9_all.tsv', sep='\t')
# v4 = pd.read_csv('V4_all.tsv', sep='\t')
# # v4_sed = pd.read_csv('V4-sediment/otu_table.no_chimera.updated.only_euks.above9.no_Metazoa_Embryophyceae.tsv', sep='\t')
# # df = pd.concat([v4, v4_sed, v9])
# df = pd.concat([v4, v9])
# # print(df)

#one OTU table
df = pd.read_csv('Amoebozoa.tsv', sep='\t')

df[['rank1', 'rank2', 'rank3', 'rank4', 'rank5', 'rank6']] = df.taxonomy.str.split('|', 5, expand=True)
# print(df['rank3'])

#SUPERGROUPS
# #SL_Euglenozoa
# total = df.groupby(['rank2']).sum().filter(regex='\d+_.*', axis=1)
# #oil_sands
# total = df.groupby(['rank2']).sum().filter(regex='.*-.*\d+', axis=1)

#SMALLER GROUPS
total = df.groupby(['rank4']).sum().filter(regex='\d+_.*', axis=1)

#change to percentages
total = (100 * total / total.sum()).round(2)

# #oil_sands
# total = total[['P1-Mar02 (201-202_S88)', 'P1-Mar02 (203-204_S89)', 'P3-Mar02 (43-44_S82)', 'P3-Mar02 (45-46_S83)', 'P3-Mar02 (49-50_S85)']]

#SL_Euglenozoa
total = total[['14_TGGTCA', '15_GTAGCC', '16_CTGATC', '17_ATTGGC',
	'1_CACTGT', '2_GATCTG', '3_GAACGA', '4_TACAAG', 
	'5_TACGGA', '6_ACATCG', '7_CCGCAT', '8_GCAGTA', 
	'11_TCAAGT', '12_AGGCCT', '13_CGTGAT',
	'9_GCTTAC', '10_GCGATT']]

# print(total)

# # total = total.filter(regex='.*MLSB.*', axis=1)
# # total = total.drop(total.filter(regex='.*SWIP.*').columns, axis=1)

transformed = total.T
# # print(transformed)
# # print(transformed.columns)
# # print(transformed.index)
# # print(transformed.size)
# # transformed = transformed.drop('V9-Oct10-2018-P3S_S72', axis=0)

# #SL_Euglenozoa
# transformed = transformed[['No_hit', 'Eukaryota_X', 
# 	'Telonemia', 'Stramenopiles', 'Alveolata', 'Rhizaria', 
# 	'Haptista', 'Cryptista', 'Archaeplastida', 
# 	'Amoebozoa', 'Obazoa', 'CRuMs', 
# 	'Metamonada', 'Discoba', 
# 	'Malawimonadidae', 'Ancyromonadida']]

# colors = ['#000000', '#A7A7A7', 
# 	'#E6AABB', '#CAB2D6', '#FB9A99', '#B2DF8A', 
# 	'#FAEBD7', '#FFFF99', '#009444', 
# 	'#1F78B4', '#C9C9C9', '#CD950B',
# 	'#7FFFD4', '#A6CEE3', 
# 	'#BCDEB4', '#FFD9C6']


# #oil_sands
# transformed = transformed[['No_hit', 'Eukaryota_X', 
# 	'Telonemia', 'Stramenopiles', 'Alveolata', 'Rhizaria', 
# 	'Haptista', 'Cryptista', 'Archaeplastida', 
# 	'Amoebozoa', 'Obazoa',
# 	'Metamonada', 'Discoba',
# 	'Ancyromonadida']]


# colors = ['#000000', '#A7A7A7', 
# 	'#E6AABB', '#CAB2D6', '#FB9A99', '#B2DF8A', 
# 	'#FAEBD7', '#FFFF99', '#009444', 
# 	'#1F78B4', '#C9C9C9',
# 	'#7FFFD4', '#A6CEE3',
# 	'#FFD9C6']

# transformed.to_csv(out_perc, sep='\t')
# # print(transformed)

ax = transformed.plot(kind='barh', stacked=True, width=0.5, align='center')
# , figsize=(7,10) , color=colors
# 
# ax.set_xlabel('OTU abundances', fontsize=5)
ax.set_xlabel('OTU abundances [%]', fontsize=10)
ax.set_ylabel('sample', fontsize=10)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
ax.xaxis.set_tick_params(width=0.5)
ax.yaxis.set_tick_params(width=0.5)
ax.xaxis.grid(True, which='major', linestyle='-', linewidth=0.25)
ax.invert_yaxis()
ax.set_axisbelow(True)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(0.6)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_linewidth(0.6)
ax.legend(bbox_to_anchor=(1, 1), loc=2, fontsize=9, frameon=False)
# ax.legend(bbox_to_anchor=(1, 1), loc='best', fontsize=4, facecolor='white', edgecolor='white', framealpha=1, frameon=True)
plt.tight_layout()
# plt.show()
# plt.savefig('discoba_counts.pdf', dpi=300)
plt.savefig('amoebozoa_percentages_new.pdf', dpi=300)
