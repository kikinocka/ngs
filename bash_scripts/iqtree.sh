#!/bin/bash

data_dir='/home/kika/MEGAsync/diplonema/catalase/apx_tree/'
aln=$data_dir'apx_trimal_0.5.aln'
guide=$data_dir'guide_apx'
guide_tree=$guide'.treefile'
bb=1000

# iqtree -m LG+F+G -nt 4 -s $aln -pre $guide
iqtree -m LG+C20+F+G -nt 4 -bb $bb -s $aln -ft $guide_tree

# iqtree -s $aln -bb $bb -nt AUTO -m TEST
# iqtree-omp -s $aln -bb $bb -nt 4 -m TEST
# -alrt $alrt -nm $nm
# nm=5000
# alrt=5000
