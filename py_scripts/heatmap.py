#!/usr/bin/python3
import os
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pylab as plt

os.chdir('/Users/kika/ownCloud/Mic60-Mgm1-Opa1/coevolution-test/')
array1 = pd.read_csv('opa1_MT_correlation.tsv', sep='\t')
array2 = pd.read_csv('mgm1_MT_correlation.tsv', sep='\t')

fig, (ax1,ax2) = plt.subplots(ncols=2)
fig.subplots_adjust(wspace=0.2)

data1 = array1.set_index('Unnamed: 0')
data1 = np.asarray(data1)
labels1 = array1.columns.values[1:]
ax1 = sns.heatmap(data1,
	vmin=0, vmax=1, 
	ax=ax1, 
	cmap='YlGnBu', cbar=False, 
	annot=True, fmt='g', 
	xticklabels=labels1, yticklabels=labels1)

data2 = array2.set_index('Unnamed: 0')
data2 = np.asarray(data2)
labels2 = array2.columns.values[1:]
ax2 = sns.heatmap(data2, 
	vmin=0, vmax=1, 
	ax=ax2, 
	cmap='YlGnBu', 
	annot=True, fmt='g', 
	xticklabels=labels2, yticklabels=labels2)

# plt.show()
plt.savefig('MT_correlation.pdf', dpi=300)



# df =  pd.DataFrame(np.random.rand(25,4), columns=list("ABCD"))
# df2 = pd.DataFrame(np.random.rand(25,4), columns=list("WXYZ"))

# fig, (ax,ax2) = plt.subplots(ncols=2)
# fig.subplots_adjust(wspace=0.01)
# sns.heatmap(df, cmap="rocket", ax=ax, cbar=False)
# fig.colorbar(ax.collections[0], ax=ax,location="left", use_gridspec=False, pad=0.2)
# sns.heatmap(df2, cmap="icefire", ax=ax2, cbar=False)
# fig.colorbar(ax2.collections[0], ax=ax2,location="right", use_gridspec=False, pad=0.2)
# ax2.yaxis.tick_right()
# ax2.tick_params(rotation=0)
# plt.show()