#!/usr/bin/env python3
import os
import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from beeswarm import *

os.chdir('/home/kika/MEGAsync/diplonema_mt/')
ypf1601 = csv.reader(open('1601/1601_module_sizes_mod.tsv'), delimiter='\t', skipinitialspace=True)
ypf1604 = csv.reader(open('1604/1604_module_sizes_mod.tsv'), delimiter='\t', skipinitialspace=True)
ypf1608 = csv.reader(open('1608/1608_module_sizes_mod.tsv'), delimiter='\t', skipinitialspace=True)
ypf1618 = csv.reader(open('1618/1618_module_sizes_mod.tsv'), delimiter='\t', skipinitialspace=True)
ypf1610 = csv.reader(open('1610/1610_module_sizes_mod.tsv'), delimiter='\t', skipinitialspace=True)
# ypf1621 = csv.reader(open('1621/1621_module_sizes_mod.tsv'), delimiter='\t', skipinitialspace=True)
papillatum = csv.reader(open('reference_strains/modules/Dpap_modules.tsv'), delimiter='\t', skipinitialspace=True)
ambulator = csv.reader(open('reference_strains/modules/Damb_modules.tsv'), delimiter='\t', skipinitialspace=True)
neradi = csv.reader(open('reference_strains/modules/Fner_modules.tsv'), delimiter='\t', skipinitialspace=True)
euleeides = csv.reader(open('reference_strains/modules/Reul_modules.tsv'), delimiter='\t', skipinitialspace=True)
# hemistasia = csv.reader(open('1610/1610_module_sizes_mod.tsv'), delimiter='\t', skipinitialspace=True)

def get_cmap(n, name='viridis'): #hsv for very divergent data?
	'''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
	RGB color; the keyword argument name must be a standard mpl colormap name.'''
	colormap = plt.cm.get_cmap(name, n)
	rgbcolors = []
	for i in range(colormap.N):
		rgb = colormap(i)[:3] # will return rgba, we take only first 3 so we get rgb
		rgbcolors.append(matplotlib.colors.rgb2hex(rgb))
	return rgbcolors

def csv_parser(file):
	module_list = []
	for row in file:
		module_list.append(int(row[1]))
	return module_list

llan = csv_parser(ypf1601)
djap = csv_parser(ypf1604)
rhum = csv_parser(ypf1608)
sspe = csv_parser(ypf1618)
ypf10 = csv_parser(ypf1610)
# ypf21 = csv_parser(ypf1621)
dpap = csv_parser(papillatum)
damb = csv_parser(ambulator)
fner = csv_parser(neradi)
reul = csv_parser(euleeides)
# hpha = csv_parser(hemistasia)

# module sizes in each species
y = [dpap, damb, fner, reul, djap, rhum, llan, sspe, ypf10]
#list of species
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

data = []
for i in y:
	data.append(np.array(i))

boxprops = dict(linestyle='-', linewidth=1, color='black')
medianprops = dict(linestyle='-', linewidth=3, color='black')
bplot = beeswarm(data, method='swarm', s=10, col='lightgray', zorder=10)
bplot = plt.boxplot(data, notch=True, patch_artist=True, boxprops=boxprops, medianprops=medianprops)

#or define: ['pink', 'lightblue', 'lightgreen']
# colors = get_cmap(len(x))
colors = ['pink', 'pink', 'pink', 'pink', 'hotpink', 'hotpink', 'hotpink', 'hotpink', 'darkcyan'] #'aquamarine', 
for patch, color in zip(bplot['boxes'], colors):
	patch.set_facecolor(color)

for xe, ye in zip(x, y):
	 plt.plot([xe] * len(ye), ye, 'o', mfc='none', c='black', zorder=10)

plt.setp(bplot['whiskers'], color='black')
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9])
plt.axes().set_xticklabels(['D. papillatum', 'D. ambulator', 'F. neradi', 'R. euleeides', \
	'D. japonicum',	'R. humris', 'L. lanifica', 'S. specki', 'YPF1610'])

plt.show()