#!/usr/bin/env python3
import openpyxl
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import matplotlib.colors as mcolors
#from google.colab import drive

#drive.mount('/content/drive')

XLSX_PATH         = '/content/drive/MyDrive/Colab_Notebooks/eukaryotes_groups.xlsx'
TOTAL_PANEL_WIDTH = 20.0
FIG_HEIGHT        = 7
YAXIS_SIZE        = 9
XAXIS_SIZE        = 10
TITLE_SIZE        = 12
CBAR_TICK_SIZE    = 10
DPI               = 300

wb = openpyxl.load_workbook(XLSX_PATH, read_only=True)
ws = wb.active
rows = [list(r) for r in ws.iter_rows(values_only=True)]

chain_row   = rows[0]
residue_row = rows[1]
aa_row      = rows[2]
data_rows   = [r for r in rows[3:] if r[0] is not None]


def fill_forward(row):
    filled, cur = [], None
    for v in row:
        if v is not None:
            cur = v
        filled.append(cur)
    return filled


chain_row_f   = fill_forward(chain_row)
residue_row_f = fill_forward(residue_row)

col_meta = []
for i in range(1, len(aa_row)):
    if aa_row[i] is None:
        continue
    col_meta.append({
        'chain'  : chain_row_f[i],
        'residue': residue_row_f[i],
        'aa'     : aa_row[i],
        'col_idx': i,
    })

residues_map  = {}
for m in col_meta:
    residues_map.setdefault(m['residue'], []).append(m)
residue_order = list(dict.fromkeys(m['residue'] for m in col_meta))
chain_of      = {r: residues_map[r][0]['chain'] for r in residue_order}

clade_names = [r[0] for r in data_rows]

# n_species: use max total count across all residues for each clade
# (avoids 0 for clades that have no data at one particular position)
n_species_per_clade = [
    max(
        sum(row[m['col_idx']] or 0 for m in residues_map[res])
        for res in residue_order
    )
    for row in data_rows
]

aa_list = 'RHKDESTNQCUGPAVILMFYW-'
n_aa    = len(aa_list)

res_matrices = {res: [] for res in residue_order}

for row in data_rows:
    for res in residue_order:
        arr = np.zeros(n_aa)
        for m in residues_map[res]:
            if m['aa'] in aa_list:
                arr[aa_list.index(m['aa'])] += row[m['col_idx']] or 0
        total = arr.sum()
        res_matrices[res].append(arr / total if total > 0 else np.zeros(n_aa))


aa_indices   = list(range(n_aa))
n_clades     = len(clade_names)
ytick_labels = [f'{g} ({n})' for g, n in zip(clade_names, n_species_per_clade)]

dark_pink = '#C71585'
ligth_pink = '#fdf7fb'
cmap_pink = mcolors.LinearSegmentedColormap.from_list("custom_pink", [ligth_pink, dark_pink])

def make_figure(res_list, title, panel_width, fig_height):

    n_res = len(res_list)
    cbar_margin = 1.2
    fig_width   = panel_width * n_res + cbar_margin

    fig, axes = plt.subplots(1, n_res, figsize=(fig_width, fig_height), sharey=True)
    if n_res == 1:
        axes = [axes]

    im = None
    for i, res in enumerate(res_list):
        ax         = axes[i]
        res_matrix = np.array(res_matrices[res])

        im = ax.imshow(res_matrix, cmap=cmap_pink, aspect='auto', vmin=0, vmax=1)

        ax.set_xticks(aa_indices)
        ax.set_xticklabels(list(aa_list), fontsize=XAXIS_SIZE)
        ax.set_yticks(np.arange(n_clades))
        ax.set_yticklabels(ytick_labels, fontsize=YAXIS_SIZE)
        ax.set_title(res, fontsize=TITLE_SIZE, fontweight='bold')
        ax.tick_params(axis='both', which='both', length=5)

        if i > 0:
            ax.tick_params(labelleft=False)

    plot_right = (fig_width - cbar_margin) / fig_width
    plt.tight_layout(rect=[0, 0, plot_right, 1])

    # Place colorbar in the reserved margin, vertically centred
    cbar_ax = fig.add_axes([plot_right + 0.01, 0.15, 0.025, 0.7])
    cbar    = fig.colorbar(im, cax=cbar_ax, orientation='vertical')
    cbar.ax.yaxis.set_major_formatter(PercentFormatter(xmax=1))
    cbar.ax.tick_params(labelsize=CBAR_TICK_SIZE)

    fig.suptitle(title, fontsize=14, fontweight='bold', y=1.02)
    return fig

chc_res = [r for r in residue_order if chain_of[r] == 'CHC']
clc_res = [r for r in residue_order if chain_of[r] == 'CLC']

plt.close('all')

chc_fig = make_figure(
    chc_res,
    title='CHC',
    panel_width=TOTAL_PANEL_WIDTH / len(chc_res),
    fig_height=FIG_HEIGHT,
)

clc_fig = make_figure(
    clc_res,
    title='CLC',
    panel_width=TOTAL_PANEL_WIDTH / len(clc_res),
    fig_height=FIG_HEIGHT,
)

chc_fig.savefig('eukaryotes_CHC_conservation.svg', dpi=DPI, bbox_inches='tight')
clc_fig.savefig('eukaryotes_CLC_conservation.svg', dpi=DPI, bbox_inches='tight')
print('Saved: eukaryotes_CHC_conservation.svg')
print('Saved: eukaryotes_CLC_conservation.svg')

plt.show()
