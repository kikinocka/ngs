#!/bin/bash

cd /mnt/mokosz/home/kika/archam_trees/cpn10

aln='cpn10.trimal_gt_0.8.aln'
# guide='guide_ak'
# guide_tree=$guide'.treefile'
bb=1000
# nm=2000
threads=10

# iqtree -m LG+F+G -nt AUTO -ntmax $threads -quiet -s $aln -pre $guide
# iqtree -m LG+C20+F+G -nt AUTO -ntmax $threads -bb $bb -quiet -s $aln -ft $guide_tree 

iqtree -m TEST -nt AUTO -ntmax $threads -bb $bb -quiet -s $aln
# -nm $nm 