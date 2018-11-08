#!/bin/sh

aln='/media/4TB1/blastocrithidia/ssu_tree/tryps_ssu_trimal_automated1.aln'
bb=1000
# alrt=5000
# nm=5000

iqtree -s $aln -bb $bb -nt 32 -m TEST

# -alrt $alrt -nm $nm