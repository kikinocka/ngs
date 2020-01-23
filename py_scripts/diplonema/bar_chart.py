#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

genes = ('atp6', 'cob', 'cox1', 'cox2', 'cox3', 'nad1', 'nad2', 'nad3', 'nad4', 'nad4L', 'nad5', 'nad6', 'nad7', 'nad8', 'nad9', 'rnl', 'rns', 'y4', 'y7')
djap = [0, 1, 1, 1, 1, 1, 3, 0, 1, 0, 2, 1, 0, 0, 1, 1, 1, 0, 0]
rhum = [0, 1, 1, 1, 1, 1, 3, 0, 0, 1, 0, 2, 0, 0, 2, 1, 1, 1, 0]
llan = [0, 1, 1, 1, 1, 1, 3, 1, 1, 1, 0, 1, 0, 1, 2, 2, 0, 2, 1]
sspe = [0, 1, 0, 1, 1, 1, 2, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 2, 0]
ypf10 = [1, 4, 4, 3, 1, 4, 7, 2, 7, 2, 8, 0, 2, 1, 1, 3, 0, 0, 0]
ypf21 = [4, 6, 10, 4, 4, 8, 9, 4, 11, 1, 14, 0, 5, 2, 4, 4, 1, 0, 0]


fig, ax = plt.subplots()
index = np.arange(len(genes))
bar_width = 0.1
 
rects1 = plt.bar(index, djap, bar_width,
				 color='#f3baba',
				 edgecolor='none',
				 label='D. japonicum')

rects2 = plt.bar(index + bar_width, rhum, bar_width,
				 color='#e35e60',
				 edgecolor='none',
				 label='R. humris')

rects3 = plt.bar(index + 2*bar_width, llan, bar_width,
				 color='#d7191c',
				 edgecolor='none',
				 label='L. lanifica')

rects4 = plt.bar(index + 3*bar_width, sspe, bar_width,
				 color='#810f10',
				 edgecolor='none',
				 label='S. specki')

rects5 = plt.bar(index + 4*bar_width, ypf10, bar_width,
				 color='#a6cee3',
				 edgecolor='none',
				 label='YPF1610')

rects6 = plt.bar(index + 5*bar_width, ypf21, bar_width,
				 color='#1f78b4',
				 edgecolor='none',
				 label='YPF1621')


plt.xlim(0, 19)
plt.xticks(index, genes, fontstyle='italic', horizontalalignment='left')
# plt.ylabel('Number of modules')
plt.legend(loc='upper right')
plt.show()
