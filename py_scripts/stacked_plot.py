#!/usr/bin/env python3
import os
import pandas as pd
import matplotlib.pyplot as plt

# os.chdir('/Users/kika/ownCloud/oil_sands/Lane26_18S_V9/identities/ver2_metamonada_cont_removed/')
# df = pd.read_csv('otu_identities.tsv', sep='\t')
# # print(df)

# # #SL_Euglenozoa
# # colors = ['#000000', '#CD950B', '#FFB90F', '#FFFF99', '#FAEBD7', 
# # 	'#CAB2D6', '#FB9A99', '#B2DF8A', '#009444', '#1F78B4',
# # 	'#C9C9C9', '#BCDEB4', '#7FFFD4', '#A6CEE3']

# #oil sands
# colors = ['#999999', '#000000', '#FFFF99', '#FAEBD7', 
# 	'#CAB2D6', '#FB9A99', '#B2DF8A', '#009444', '#1F78B4',
# 	'#C9C9C9', '#7FFFD4', '#A6CEE3']

# ax = df.plot(x='perc', kind='bar', stacked=True, color=colors, width=0.5, align='center')
# ax.set_xticklabels(df.perc, rotation=0)
# ax.xaxis.set_tick_params(width=0.5)
# ax.yaxis.set_tick_params(width=0.5)
# ax.set_xlabel('Similarity to reference sequences [%]')
# ax.set_ylabel('OTU count')
# ax.yaxis.grid(True, which='major', linestyle='-', linewidth=0.25)
# ax.set_axisbelow(True)
# ax.spines['right'].set_visible(False)
# ax.spines['left'].set_linewidth(0.6)
# ax.spines['top'].set_visible(False)
# ax.spines['bottom'].set_linewidth(0.6)
# ax.legend(bbox_to_anchor=(1, 1), frameon=False)
# plt.tight_layout()
# # plt.show()
# plt.savefig('otu_identities.pdf', dpi=300)


os.chdir('/Users/kika/ownCloud/SL_Euglenozoa/V9/above99_decontaminated/supergroups/')
df = pd.read_csv('v9_supergroups.no_chimera.above99.no_prokaryota.tsv', sep='\t')
# print(df)

#SL_Euglenozoa
colors = ['#000000', '#999999', '#CD950B', '#FFB90F', '#FFFF99', 
	'#FAEBD7', '#CAB2D6', '#FB9A99', '#B2DF8A', '#009444',
	'#1F78B4', '#C9C9C9', '#7FFFD4', '#A6CEE3']

# #oil sands
# colors = ['#999999', '#000000', '#FFFF99', '#FAEBD7', 
# 	'#CAB2D6', '#FB9A99', '#B2DF8A', '#009444', '#1F78B4',
# 	'#C9C9C9', '#7FFFD4', '#A6CEE3']

# #metamonads
# colors = [
# 	'#4c4c4c', 
# 	'#e5fff6', '#cbffed', '#b2ffe5', '#7fffd4', '#65cca9', '#4c997f', '#326654', '#19332a',
# 	'#7f7f7f', 
# 	'#cccccc', 
# 	'#fdf3f5', '#f9d1d8', '#f5afbb', '#f18d9e', '#c0707e', '#90545e', '#301c1f', 
# 	'#c7cceb', '#9099d8', '#4655bf', '#2a3372', 
# 	'#8a8119', '#e6d72a']

ax = df.plot(x='sample', kind='barh', stacked=True, color=colors, width=0.5, align='center')
ax.set_xlabel('OTU abundances', fontsize=8)
ax.set_ylabel('sample', fontsize=8)
plt.xticks(fontsize=6)
plt.yticks(fontsize=6)
ax.xaxis.set_tick_params(width=0.5)
ax.yaxis.set_tick_params(width=0.5)
ax.xaxis.grid(True, which='major', linestyle='-', linewidth=0.25)
ax.invert_yaxis()
ax.set_axisbelow(True)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(0.6)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_linewidth(0.6)
ax.legend(bbox_to_anchor=(1, 1), loc=2, fontsize=6, frameon=False)
plt.tight_layout()
# plt.show()
plt.savefig('v9_supergroups.no_chimera.above99.no_prokaryota.pdf', dpi=300)
