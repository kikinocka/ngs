#!/usr/bin/env python3
import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir('/Users/kika/ownCloud/oil_sands/')
v9 = pd.read_csv('Lane26_18S_V9/otu_table.updated.tsv', sep='\t')
v4 = pd.read_csv('18S-V4-2018/otu_table.updated.tsv', sep='\t')
df = pd.concat([v4, v9])
with open('otu_table.concat.tsv', 'w') as out:
	df.to_csv(out, sep='\t')

# df[['rank1', 'rank2', 'rank3']] = df.lineage.str.split('|', 2, expand=True)

# #supergroups
# total = df.groupby(['rank2']).sum().filter(regex='.*_S\d+', axis=1)
# transformed = total.T
# # print(transformed)
# # print(transformed.columns)
# # print(transformed.index)
# # print(transformed.size)
# # total = transformed.drop('V9-Oct10-2018-P3S_S72', axis=0)

# transformed = transformed[['No_hit', 'Eukaryota_X', 'Cryptista', 'Haptista', 'Stramenopiles', 'Alveolata', 'Rhizaria',
# 	'Archaeplastida', 'Amoebozoa', 'Obazoa', 'Metamonada', 'Discoba']]
# # print(transformed)

# colors = ['#999999', '#000000', '#FFFF99', '#FAEBD7', 
# 	'#CAB2D6', '#FB9A99', '#B2DF8A', '#009444', '#1F78B4',
# 	'#C9C9C9', '#7FFFD4', '#A6CEE3']

# # #SL_Euglenozoa
# # colors = ['#000000', '#CD950B', '#FFB90F', '#FFFF99', '#FAEBD7', 
# # 	'#CAB2D6', '#FB9A99', '#B2DF8A', '#009444', '#1F78B4',
# # 	'#C9C9C9', '#BCDEB4', '#7FFFD4', '#A6CEE3']


# # # #metamonads
# # meta = df[df.rank3.isin(['Metamonada'])]
# # meta['species'] = meta.lineage.apply(lambda x: x.split('Metamonada_X|')[1])
# # grouped = meta.groupby(['species']).sum().filter(regex='V9.*', axis=1)
# # transformed = grouped.T
# # # print(meta)

# # colors = [
# # 	'#c7cceb', '#9099d8', '#4655bf', '#2a3372', 
# # 	'#4c4c4c', 
# # 	'#e5fff6', '#cbffed', '#b2ffe5', '#7fffd4', '#65cca9', '#4c997f', '#326654', '#19332a',
# # 	'#7f7f7f', 
# # 	'#fdf3f5', '#f9d1d8', '#f5afbb', '#f18d9e', '#c0707e', '#90545e', '#301c1f', 
# # 	'#8a8119', '#e6d72a']

# ax = transformed.plot(kind='barh', stacked=True, color=colors, width=0.5, align='center')
# ax.set_xlabel('OTU abundances', fontsize=5)
# ax.set_ylabel('sample', fontsize=5)
# plt.xticks(fontsize=4)
# plt.yticks(fontsize=4)
# ax.xaxis.set_tick_params(width=0.5)
# ax.yaxis.set_tick_params(width=0.5)
# ax.xaxis.grid(True, which='major', linestyle='-', linewidth=0.25)
# ax.invert_yaxis()
# ax.set_axisbelow(True)
# ax.spines['right'].set_visible(False)
# ax.spines['left'].set_linewidth(0.6)
# ax.spines['top'].set_visible(False)
# ax.spines['bottom'].set_linewidth(0.6)
# ax.legend(bbox_to_anchor=(1, 1), loc=2, fontsize=4, frameon=False)
# # ax.legend(bbox_to_anchor=(1, 1), loc='best', fontsize=4, facecolor='white', edgecolor='white', framealpha=1, frameon=True)
# plt.tight_layout()
# # plt.show()
# plt.savefig('supergroups.pdf', dpi=300)
