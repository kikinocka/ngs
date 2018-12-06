#!/bin/bash

aln='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Fd+FNR/chlamydial/fd_trimal_0.3.aln'
bb=1000
alrt=5000
nm=5000

iqtree-omp -s $aln -bb $bb -nt 4 -m TEST

# -alrt $alrt -nm $nm