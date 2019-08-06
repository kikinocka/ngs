#!/bin/bash

data_dir='/home/kika/ownCloud/pelomyxa_schiedti/mito_proteins/fes_cluster_assembly/nif/nifU_tree/pmsf_without_iscU/'
aln=$data_dir'nifU_trimal_automated1.aln'
guide=$data_dir'guide_nifU'
guide_tree=$data_dir$guide'.treefile'
bb=1000

iqtree -m LG+F+G -nt 4 -s $aln -pre $guide
iqtree -m LG+C20+F+G -nt 4 -bb $bb -s $aln -ft $guide_tree

# iqtree -s $aln -bb $bb -nt AUTO -m TEST
# iqtree-omp -s $aln -bb $bb -nt 4 -m TEST
# -alrt $alrt -nm $nm
# nm=5000
# alrt=5000
