#!/bin/bash

cd /mnt/mokosz/home/kika/pelomyxa_schiedti/trees/vdac/ver2/

aln='porins.trimal_gt-0.8.aln'
guide='guide_porins'
guide_tree=$guide'.treefile'
bb=1000
nm=5000
threads=10

iqtree -m LG+F+G -nt AUTO -ntmax $threads -quiet -s $aln -pre $guide
iqtree -m LG+C20+F+G -nt AUTO -ntmax $threads -bb $bb -nm $nm -quiet -s $aln -ft $guide_tree 

# iqtree -m TEST -nt AUTO -ntmax $threads -bb $bb -quiet -s $aln
# -nm $nm 
