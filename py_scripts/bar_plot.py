#!/usr/bin/env python3
import os
import numpy as np
import matplotlib.pyplot as plt

# os.chdir('/home/kika/MEGAsync/Manuscripts/Euglenozoa_CAT-APX/')

# f, (ax, ax2) = plt.subplots(2, 1, sharex=True)
fig, ax = plt.subplots()

species = ['DPr', 'DPp', 'RH', 'BP57', 'LS14', 'LS23', 'LS34', 'CT14', 'CT23', 'CT34', 'NE', 'TB', 'EG', 'EL']

# #APX activity
# value = [0, 0, 0, 4, 5.3, 0, 0, 6.3, 4.3, 4.3, 20, 0, 5100, 0]
# std = [0, 0, 0, 1, 2, 0, 0, 0.4, 1.8, 1.8, 10, 0, 270, 0]
#APX transcripts
value = [0, 0, 0, 0, 164, 16.7, 41.5, 181, 18, 27.7, 73.8, 0, 40.3, 0]
# #CAT activity
# value = [2, 1.8, 0, 0, 16.3, 17.4, 8, 21, 13.3, 5.3, 9, 0, 0, 0]
# std = [0.1, 0.2, 0, 0, 2.1, 1.4, 0.6, 0.2, 0.3, 0.5, 0.8, 0, 0, 0]
# #CAT transcripts
# value = [216.2, 256.9, 25.4, 26.9, 813.5, 116.8, 432.9, 567.6, 678.9, 972.9, 626.2, 0, 0, 0]
# #Respiration
# value = [2.4, 7.8, 12.5, 2.5, 5.8, 8.9, 7.9, 6.2, 10.9, 11.8, 2.7, 2.4, 16.9, 23.6]
# std = [0.9, 2.5, 1.3, 0.6, 0.8, 0.4, 0.5, 0.1, 2.7, 1, 0.7, 1.1, 2.9, 3.3]

#ONE GRAPH
# plot the same data on both axes
ax.bar(species, value, color='lightgrey')
plt.ylabel('APX transcripts [TPM]')
plt.show()

# #TWO GRAPHS IN ONE FIGURE
# # plot the same data on both axes
# ax.bar(species, value, color='lightgrey', yerr=std, capsize=3)
# ax2.bar(species, value, color='lightgrey', yerr=std, capsize=3)

# # zoom-in / limit the view to different portions of the data
# ax.set_ylim(4500, 5500) # outliers
# ax2.set_ylim(0, 35) # most of the data

# # hide the spines between ax and ax2
# ax.spines['bottom'].set_visible(False)
# ax2.spines['top'].set_visible(False)
# ax.xaxis.tick_top()
# ax.tick_params(labeltop='off') # don't put tick labels at the top
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

# plt.ylabel('CAT transcripts [TPM]')
# plt.show()
# # plt.savefig('apx_activity.svg', dpi=600)

