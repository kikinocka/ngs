#!/bin/sh

aln='/media/4TB1/blastocrithidia/kika_workdir/trnas_deduplicated_anticodon.aln'
bb=5000
alrt=5000
nm=5000

/home/nenarokova/tools/iqtree-omp-1.5.3-Linux/bin/iqtree-omp -s $aln -bb $bb -alrt $alrt -nm $nm -nt AUTO