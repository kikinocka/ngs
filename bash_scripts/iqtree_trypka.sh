#!/bin/sh

aln='/home/kika/work_dir/nr70_trimal_automated1.aln'
bb=1000
# alrt=5000
# nm=5000

/home/nenarokova/tools/iqtree-omp-1.5.3-Linux/bin/iqtree-omp -s $aln -bb $bb -nt 30 -m TEST

# -alrt $alrt -nm $nm