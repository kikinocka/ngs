#!/bin/bash

cd /mnt/mokosz/home/kika/workdir/

aln='NR.trimal_gt_0.8.aln'
guide='guide_NR'
guide_tree=$guide'.treefile'
bb=1000
threads=15

iqtree -m LG+F+G -nt AUTO -ntmax $threads -quiet -s $aln -pre $guide
iqtree -m LG+C20+F+G -nt AUTO -ntmax $threads -bb $bb -quiet -s $aln -ft $guide_tree 
