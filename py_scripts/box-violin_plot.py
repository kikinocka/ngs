#!/usr/bin/env python3
import os
import seaborn as sns
import pandas as pd
import matplotlib.pylab as plt

os.chdir('/Users/kika/ownCloud/plastid_genomes/')
df = pd.read_excel('genomes_genes.xlsx', sheet_name='genomes')
# print(df)

fig, ax = plt.subplots(figsize=(18, 16))

# sns.violinplot(x=df['higher taxon'], y=df['length'], width=1.75)
sns.boxplot(x=df['higher taxon'], y=df['length'], \
	flierprops={'marker': 'o', 'markerfacecolor': 'lightgrey', 'markeredgecolor': 'grey'})
ax.tick_params(axis='x', labelrotation=90)
ax.set_ylim(0, 500000)

# plt.show()
# plt.savefig('violins.pdf', dpi=300)
plt.savefig('genome_sizes.svg', dpi=300)
