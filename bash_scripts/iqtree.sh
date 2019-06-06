#!/bin/bash

aln='/home/kika/ownCloud/euglenophytes/trees/q1010219/q1010219_trimal_automated1.aln'
bb=1000
alrt=5000
nm=5000

iqtree-omp -s $aln -bb $bb -nt 4 -m TEST

# -alrt $alrt -nm $nm