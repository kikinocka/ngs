#!/bin/bash

data_dir='/home/kika/MEGAsync/diplonema_paramylon/beta-1,3-glucan_synthase/domain/'
aln=$data_dir'glucane_synthase_trimal_0.5.aln'
guide=$data_dir'guide_glucane_synthase'
guide_tree=$data_dir$guide'.treefile'

iqtree-omp -m LG+F+G -nt 4 -s $aln -pre $guide
iqtree-omp -m LG+C20+F+G -nt 4 -bb $bb -s $aln -ft $guide_tree

# iqtree -s $aln -bb $bb -nt AUTO -m TEST
# iqtree-omp -s $aln -bb $bb -nt 4 -m TEST
# -alrt $alrt -nm $nm
# nm=5000
# alrt=5000
