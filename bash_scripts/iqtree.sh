#!/bin/bash

work_dir='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/sec/secA/'
aln=$work_dir'secA_trimal_automated1.aln'
bb=1000
alrt=5000
nm=5000

iqtree-omp -s $aln -bb $bb -nt 4 -m TEST

# -alrt $alrt -nm $nm