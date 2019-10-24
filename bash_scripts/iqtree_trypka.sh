#!/bin/sh

datadir='/home/kika/work_dir/'
aln=$datadir'apx_trimal_0.5.aln'
guide=$datadir'guide_apx'
guide_tree=$datadir$guide'.treefile'
bb=1000
# alrt=5000
# nm=5000

# iqtree -s $aln -bb $bb -nt AUTO -m TEST
# -alrt $alrt -nm $nm

iqtree -m LG+F+G -nt AUTO -ntmax 30 -quiet -s $aln -pre $guide
iqtree -m LG+C20+F+G -nt AUTO -ntmax 30 -bb $bb -quiet -s $aln -ft $guide_tree
