#!/usr/bin/env python3
import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir('/Users/kika/ownCloud/oil_sands/amplicons/')

#several OTU tables
v9 = pd.read_csv('Lane26_18S_V9/otu_table.no_chimera.updated.only_euks.above99.no_Metazoa_Embryophyceae.tsv', sep='\t')
v4 = pd.read_csv('18S-V4-2018/otu_table.no_chimera.updated.only_euks.above99.no_Metazoa_Embryophyceae.tsv', sep='\t')
v4_sed = pd.read_csv('V4-sediment/otu_table.no_chimera.updated.only_euks.above99.no_Metazoa_Embryophyceae.tsv', sep='\t')
df = pd.concat([v4, v4_sed, v9])
print(df)

#one OTU table
# df = pd.read_csv('otu_table.no_chimera.updated.only_euks.above99.tsv', sep='\t')

df[['rank1', 'rank2', 'rank3', 'rank4', 'rank5']] = df.taxonomy.str.split('|', 4, expand=True)
# print(df['rank3'])

#SUPERGROUPS
# #SL_Euglenozoa
# total = df.groupby(['rank2']).sum().filter(regex='\d+_.*', axis=1)
#oil_sands
total = df.groupby(['rank2']).sum().filter(regex='.*_S\d+', axis=1)

# #SMALLER GROUPS
# total = df.groupby(['rank3']).sum().filter(regex='\d+_.*', axis=1)

#change to percentages
total = (100 * total / total.sum()).round(2)

#oil_sands
total = total[['L16Feb12P10m_S209', 'V9-Feb12-2018-P1-0m_S9', 'V9-Feb12-2018-P1-2m_S10', 'L16Feb12P14m_S211', 
	'V9-Feb12-2018-P1-4m_S11', 'V9-Feb12-2018-P1-6m_S12', 'L16Feb12P18m_S213', 'V9-Feb12-2018-P1-8m_S13', 'L16Feb12P1bot_S214', 
	'V9-Feb12-2018-P1B_S14', 'V9-Feb12-2018-P2-4m_S17', 'L16Feb12P26m_S218', 'V9-Feb12-2018-P2-6m_S18', 'L16Feb12P28m_S219', 
	'V9-Feb12-2018-P2-8m_S19', 'L16Feb12P38m_S226', 'V9-Feb12-2018-P3-8m_S24', 'V9-Feb12-2018-P2-10m_S20', 'L16Mr12P24m_S255', 
	'V9-Mr12-2018-P2-4m_S25', 'L16Mr12P28m_S257', 'V9-Mr12-2018-P2-8m_S26', 'L16Mr12P38m_S263', 'V9-Mr12-2018-P3-8m_S30', 
	'L17BMLJuly23P1B_S103', 'V9-July23-2018-P1B_S39', 'L17BMLJuly23P1S_S101', 'V9-July23-2018-P1S_S38', 'L17BMLJuly23P2B_S104', 
	'L17BMLJuly23P2S_S102', 'V9-July23-2018-P2S_S40', 'L17BMLJuly23P3B_S106', 'V9-July23-2018-P3B_S43', 'L17BMLJuly23P3S_S105', 
	'V9-July23-2018-P3S_S42', 'L17BMLAu13P1B_S135', 'L17BMLAu13P1S_S134', 'V9-Aug13-2018-P1S_S44', 'L17BMLAu13P2B_S137', 
	'V9-Aug13-2018-P2B_S47', 'L17BMLAu13P2S_S136', 'V9-Aug13-2018-P2S_S46', 'L17Au13P3B_S139', 'V9-Aug13-2018-P3B_S49', 
	'L17BMLAu13P3S_S138', 'L22Sept1018P1B_S114', 'V9-Sept13-2018-P1B_S61', 'L22Sept1018P1S_S113', 'V9-Sept13-2018-P1S_S60', 
	'L22Sept1018P2B_S116', 'V9-Sept13-2018-P2B_S63', 'L22Sept1018P2S_S115', 'V9-Sept13-2018-P2S_S62', 'L22Sept1018P3B_S118', 
	'L22Sept1018P3S_S117', 
	'201-202-P1-2017Mr2_S286', 'V9-201-202-P1-2017_S88', '203-204-P1-2017Mr2_S287', 'V9-203-204-P1-2017_S89', 
	'43-44-P3-2017Mr2_S191', 'V9-43-44-P3-2017_S82', '45-45-P3-2017Mr2_S192', 'V9-45-46-P3-2017_S83', '49-50-P3-2017Mr2_S285', 
	'V9-49-50-P3-2017_S85', 
	'L17May28MLSB_S44', 'V9-MLSB-May30-2018_S6', 'L17June4MLSB_S52', 'L17June11MLSB_S60', 'L17June18MLSB_S68', 
	'V9-MLSB-June18-2018_S33', 'L17July3MLSB_S84', 'L17July16MLSB_S99', 'L20MLSBAug1518_S157', 'L20MLSBAug2718_S165', 
	'L22MLSBSept42010_S171', 'V9-MLSB-Sep04-2010_S2', 'L22MLSBSept1018_S120', 'V9-MLSB-Sept13-2018_S67', 'L22MLSBSept2418_S136', 
	'V9-MLSB-Sept24-2018_S58', 'L22MLSBOct918_S151', 'V9-MLSB-Oct10-2018_S75', 'L22MLSBNov62018_S182', 'V9-MLSB-Nov06-2018_S77', 
	'L22MLSBNov192018_S183', 'V9-MLSB-Nov14-2018_S79', 'V9-MLSB-Nov17-2018_S81', 'L22MLSBNov232010_S172', 'V9-MLSB-Nov23-2010_S4', 
	'L17May28BCR_S45', 'V9-BCR-May30-2018_S5', 'L17June4BCR_S53', 'V9-BCR-June04-2018_S7', 'L17June18BCR_S69', 
	'V9-BCR-June18-2018_S32', 'L17July3BCR_S85', 'V9-BCR-July03-2018_S34', 'L17July16BCR_S100', 'V9-BCR-July16-2018_S36', 
	'L20BCRAug2018_S158', 'V9-BCR-pIN-Aug20-2018_S55', 'L20BCRAug2718_S166', 'L22BCRinSept1018_S119', 'V9-BCR-pIN-Sept12-2018_S56', 
	'L22BCRLauOct118_S152', 'V9-BCR-boat-Oct10-2018_S59', 
	'L22WIPSept42010_S169', 'V9-WIP-Sept04-2010_S1', 'L22WIPNov232010_S170', 'V9-WIP-Nov23-2010_S3', 'L22SWIPAug152018_S173', 
	'V9-SWIP-Aug13-2018_S50', 'L22SWIPAug272018_S174', 'V9-SWIP-Aug27-2018_S52', 'L22SWIPSept102018_S175', 'V9-SWIP-Sept13-2018_S66', 
	'V9-SWIP-Sept24-2018_S57', 'L22SWIPNov62018_S179', 'V9-SWIP-Nov06-2018_S76', 'L22SWIPNov192018_S180', 'V9-SWIP-Nov14-2018_S78', 
	'V9-SWIP-Nov17-2018_S80']]
# print(total)

# #SL_Euglenozoa
# total = total[['14_TGGTCA', '15_GTAGCC', '16_CTGATC', '17_ATTGGC',
# 	'1_CACTGT', '2_GATCTG', '3_GAACGA', '4_TACAAG', 
# 	'5_TACGGA', '6_ACATCG', '7_CCGCAT', '8_GCAGTA', 
# 	'11_TCAAGT', '12_AGGCCT', '13_CGTGAT',
# 	'9_GCTTAC', '10_GCGATT']]

# total = total.filter(regex='.*MLSB.*', axis=1)
# total = total.drop(total.filter(regex='.*SWIP.*').columns, axis=1)

transformed = total.T
# print(transformed)
# print(transformed.columns)
# print(transformed.index)
# print(transformed.size)
# transformed = transformed.drop('V9-Oct10-2018-P3S_S72', axis=0)

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


#oil_sands
transformed = transformed[['Eukaryota_X', 
	'Stramenopiles', 'Alveolata', 'Rhizaria', 
	'Haptista', 'Cryptista', 'Archaeplastida', 
	'Amoebozoa', 'Obazoa',
	'Metamonada', 'Discoba']]

colors = ['#A7A7A7', 
	'#CAB2D6', '#FB9A99', '#B2DF8A', 
	'#FAEBD7', '#FFFF99', '#009444', 
	'#1F78B4', '#C9C9C9',
	'#7FFFD4', '#A6CEE3']


ax = transformed.plot(kind='barh', stacked=True, color=colors, width=0.5, align='center', figsize=(7,10))
# ax = transformed.plot(kind='barh', stacked=True, width=0.5, align='center')
# 
# ax.set_xlabel('OTU abundances', fontsize=5)
ax.set_xlabel('OTU abundances [%]', fontsize=5)
ax.set_ylabel('sample', fontsize=5)
plt.xticks(fontsize=4)
plt.yticks(fontsize=4)
ax.xaxis.set_tick_params(width=0.5)
ax.yaxis.set_tick_params(width=0.5)
ax.xaxis.grid(True, which='major', linestyle='-', linewidth=0.25)
ax.invert_yaxis()
ax.set_axisbelow(True)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(0.6)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_linewidth(0.6)
ax.legend(bbox_to_anchor=(1, 1), loc=2, fontsize=4, frameon=False)
# ax.legend(bbox_to_anchor=(1, 1), loc='best', fontsize=4, facecolor='white', edgecolor='white', framealpha=1, frameon=True)
plt.tight_layout()
# plt.show()
# plt.savefig('supergroups/supergroups_counts.above99.no_Metazoa_Embryophyceae.pdf', dpi=300)
plt.savefig('supergroups/supergroups_percentages.above99.no_Metazoa_Embryophyceae.pdf', dpi=300)
