#!/usr/bin/env python3
import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir('/Users/kika/ownCloud/diplonema/pyruvate_metabolism/PDH/')
df = pd.read_csv('pdh_activity.tsv', sep='\t')

# fig, ax = plt.subplots()
# f, (ax, ax2) = plt.subplots(2, 1, sharex=True)

# species = ['DPr', 'DPp', 'RH', 'BP57', 'LS14', 'LS23', 'LS34', 'CT14', 'CT23', 'CT34', 'NE', 'TB', 'EGl', 'EGd', 'EL']
# species = ['PpR', 'PpP', 'Tb', 'Ps', 'Eg', 'El']
# value = [2.15, 1.43, 700, 0, 1850]
# std = [3.070351868, 8.48128787, 35.03546424, 1.498108103, 0.640051959, 1.390970518]


#ONE GRAPH
species = list(df.iloc[:, 0])
# value = list(df.iloc[:, 1])
std = list(df.iloc[:, 2])
ax = df.plot(x='species', yerr='std', kind='bar', color='#E55500', align='center', legend = False, capsize=3)
ax.set_xlabel('species')
ax.set_ylabel('mU/mg')
ax.xaxis.set_tick_params(rotation=0)
# plt.show()
plt.savefig('pdh_activity.pdf', dpi=300)


# #TWO GRAPHS IN ONE FIGURE
# # plot the same data on both axes
# ax.bar(species, value, color='lightgrey', capsize=3)
# ax2.bar(species, value, color='lightgrey', capsize=3)

# # zoom-in / limit the view to different portions of the data
# ax.set_ylim(0, 2000000) # outliers
# ax2.set_ylim(0, 2000) # most of the data

# # hide the spines between ax and ax2
# ax.spines['bottom'].set_visible(False)
# ax2.spines['top'].set_visible(False)
# ax.xaxis.tick_top()
# # ax.tick_params(labeltop='off') # don't put tick labels at the top
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

# plt.ylabel('DPM in 5 x 10^6 cells')
# # plt.show()
# plt.savefig('glu.pdf', dpi=300)
