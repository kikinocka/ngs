#!/usr/bin/env python3
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.chdir('/Users/kika/ownCloud/manuscripts/33_IDH_kinetoplastids/graphs/')
df = pd.read_csv('nadp.tsv', sep='\t')

#ONE GRAPH
fig, ax = plt.subplots(figsize=(15, 5))

species = list(df.iloc[:, 0])
nad = list(df.iloc[:, 1])
nad_std = list(df.iloc[:, 2])
nadp = list(df.iloc[:, 3])
nadp_std = list(df.iloc[:, 4])
# cell = list(df.iloc[:, 5])
# cell_std = list(df.iloc[:, 6])

# colors = [['#E55500', '#DD8558', '#BCBEC0'],
# 		['#F29C00', '#D8A14A', '#BCBEC0'],
# 		['#F2E500', '#D1C74E', '#BCBEC0']]

x_axis = np.arange(len(species))
plt.bar(x_axis - 0.2, nad, 0.4, yerr=nad_std, align='center', color='#bbbdbf', error_kw=dict(lw=0.75, capthick=0.75, capsize=2), label='cytosol')
plt.bar(x_axis + 0.2, nadp, 0.4, yerr=nadp_std, align='center', color='#7cd7f7', error_kw=dict(lw=0.75, capthick=0.75, capsize=2), label='mitochondrion')
# plt.bar(x_axis + 0.2, cell, 0.2, yerr=cell_std, capsize=3, label='cell', color=colors[0][2])
plt.xticks(x_axis, species, rotation=45)
# plt.ylim([0,850000])
plt.legend(frameon=False)
# plt.title('E1')
# plt.show()
plt.savefig('nadp.pdf', dpi=300)


# #TWO GRAPHS
# f, (ax, ax2) = plt.subplots(2, 1, figsize=(15, 5), sharex=True)

# # plot the same data on both axes
# species = df['species']
# nad = list(df.iloc[:,1])
# nad_std = list(df.iloc[:,2])
# nadp = list(df.iloc[:,3])
# nadp_std = list(df.iloc[:,4])

# x_axis = np.arange(len(species))
# ax.bar(x_axis - 0.2, nad, 0.4, yerr=nad_std, align='center', color='#ff66cc', error_kw=dict(lw=0.75, capthick=0.75, capsize=2), label='NAD+-dependent')
# ax.bar(x_axis + 0.2, nadp, 0.4, yerr=nadp_std, align='center', color='#cc66ff', error_kw=dict(lw=0.75, capthick=0.75, capsize=2), label='NADP+-dependent')
# ax2.bar(x_axis - 0.2, nad, 0.4, yerr=nad_std, align='center', color='#ff66cc', error_kw=dict(lw=0.75, capthick=0.75, capsize=2), label='NAD+-dependent')
# ax2.bar(x_axis + 0.2, nadp, 0.4, yerr=nadp_std, align='center', color='#cc66ff', error_kw=dict(lw=0.75, capthick=0.75, capsize=2), label='NADP+-dependent')

# # zoom-in / limit the view to different portions of the data
# ax.set_ylim(25.1, 250) # outliers
# ax2.set_ylim(0, 25) # most of the data

# # hide the spines between ax and ax2
# ax.spines['bottom'].set_visible(False)
# ax2.spines['top'].set_visible(False)
# ax.xaxis.tick_top()
# # ax.tick_params(labeltop=False, axis='x') # don't put tick labels at the top
# ax2.tick_params(labeltop=False, axis='x', rotation=45) # don't put tick labels at the top
# ax2.xaxis.tick_bottom()

# d = .005 # how big to make the diagonal lines in axes coordinates
# # arguments to pass to plot, just so we don't keep repeating them
# kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
# ax.plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
# ax.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal
# # switch to the bottom axes
# kwargs.update(transform=ax2.transAxes)  
# ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
# ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal

# # plt.ylabel('DPM in 5 x 10^6 cells')
# ax.set(xticks=x_axis, xticklabels=species)
# ax.legend(frameon=False)
# # plt.show()
# plt.savefig('mito.pdf', dpi=300)
