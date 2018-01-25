#!/bin/sh

aln='/home/kika/MEGAsync/blasto_project/genes/tRNAs/iqtree/untrimmed_anticodon_5000bb/trnas_deduplicated_anticodon.aln'
bb=5000
alrt=5000
nm=5000

iqtree-omp -s $aln -bb $bb -alrt $alrt -nm $nm -nt 4