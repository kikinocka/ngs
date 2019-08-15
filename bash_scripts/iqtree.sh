#!/bin/bash

data_dir='/home/kika/ownCloud/euglenophytes/replication/'
aln=$data_dir'helicases_trimal_automated1.aln'
guide=$data_dir'guide_helicases'
guide_tree=$data_dir$guide'.treefile'
bb=1000

iqtree -m LG+F+G -nt 4 -s $aln -pre $guide
iqtree -m LG+C20+F+G -nt 4 -bb $bb -s $aln -ft $guide_tree

# iqtree -s $aln -bb $bb -nt AUTO -m TEST
# iqtree-omp -s $aln -bb $bb -nt 4 -m TEST
# -alrt $alrt -nm $nm
# nm=5000
# alrt=5000
