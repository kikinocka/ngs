#!/usr/bin/env python3
import os
import numpy as np
import matplotlib.pyplot as plt

os.chdir('/Users/kika/ownCloud/manuscripts/diplonema_metabolism/figures/')

# f, (ax, ax2) = plt.subplots(2, 1, sharex=True)
fig, ax = plt.subplots()

# species = ['DPr', 'DPp', 'RH', 'BP57', 'LS14', 'LS23', 'LS34', 'CT14', 'CT23', 'CT34', 'NE', 'TB', 'EGl', 'EGd', 'EL']
species = ['R+', 'R-', 'P+', 'P-']

# #APX activity
# value = [0, 0, 3.69, 2.06, 54.26, 39.79, 34.35, 65.40, 48.63, 51.57, 206.63, 0, 625.22, 0, 0]
# std = [0, 0, 1.80, 1.84, 21.32, 10.96, 7.93, 28.87, 19.51, 27.44, 69.37, 0, 176.36, 0, 0]
# #APX transcripts
# value = [0, 0, 0, 0, 164, 16.7, 41.5, 181, 18, 27.7, 73.8, 0, 13.8, 9.9, 0]
# #CAT activity
# value = [3.99, 6.27, 0.66, 0, 16.84, 12.90, 5.07, 17.19, 13.19, 4.79, 10.76, 0, 0, 0, 0]
# std = [1.48, 3.47, 0.26, 0, 1.94, 6.48, 3.81, 6.06, 2.43, 1.11, 2.43, 0, 0, 0, 0]
# #CAT transcripts
# value = [216.2, 256.9, 25.4, 26.9, 813.5, 116.8, 432.9, 567.6, 678.9, 972.9, 626.2, 0, 0, 0, 0]
#Respiration
# value = [2.42, 7.83, 15.42, 2.44, 5.84, 8.93, 7.86, 6.21, 10.92, 11.82, 4.78, 2.95, 2.37, 15.81, 23.65]
# std = [0.98, 2.81, 6.09, 0.67, 0.90, 0.52, 0.61, 0.16, 3.15, 1.16, 0.20, 0.67, 1.22, 4.42, 3.69]
value = [102.2131826, 20.06802721, 102.5046382, 74.56828885]
std = [4.99862107, 7.823129252, 29.83920841, 23.15975443]


#ONE GRAPH
# ax.bar(species, value, color='lightgrey')
# plt.ylabel('CAT transcripts [TPM]')
ax.bar(species, value, color='lightgrey', yerr=std, capsize=3)
ax.set_ylim(0, 140)
# plt.ylabel('CAT activity [U/mg]')
plt.ylabel('U/mg')
# plt.show()
plt.savefig('sdh.pdf', dpi=300)


# #TWO GRAPHS IN ONE FIGURE
# # plot the same data on both axes
# ax.bar(species, value, color='lightgrey', yerr=std, capsize=3)
# ax2.bar(species, value, color='lightgrey', yerr=std, capsize=3)

# # zoom-in / limit the view to different portions of the data
# ax.set_ylim(3000, 2300000) # outliers
# ax2.set_ylim(0, 1800) # most of the data

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

# plt.ylabel('DPM in 5*106 cells')
# plt.show()
# # plt.savefig('14C-glucose.pdf', dpi=300)
