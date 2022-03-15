#!/usr/bin/env python3
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.chdir('/Users/kika/ownCloud/diplonema/pyruvate_metabolism/PDH/')
df = pd.read_csv('pdh_frac.tsv', sep='\t')

proteins = list(df.iloc[:, 0])
mito = list(df.iloc[:, 1])
mito_std = list(df.iloc[:, 2])
cyto = list(df.iloc[:, 3])
cyto_std = list(df.iloc[:, 4])
cell = list(df.iloc[:, 5])
cell_std = list(df.iloc[:, 6])

colors = [['#E55500', '#DD8558', '#BCBEC0'],
		['#F29C00', '#D8A14A', '#BCBEC0'],
		['#F2E500', '#D1C74E', '#BCBEC0']]

x_axis = np.arange(len(proteins))
plt.bar(x_axis - 0.2, mito, 0.2, yerr=mito_std, capsize=3, label='mito', color=colors[2][0])
plt.bar(x_axis - 0.0, cyto, 0.2, yerr=cyto_std, capsize=3, label='cyto', color=colors[2][1])
plt.bar(x_axis + 0.2, cell, 0.2, yerr=cell_std, capsize=3, label='cell', color=colors[2][2])
plt.xticks(x_axis, proteins, rotation=10)
plt.legend(frameon=False)
plt.title('PDH')
plt.show()
# plt.savefig('bckdh_frac.pdf', dpi=300)
