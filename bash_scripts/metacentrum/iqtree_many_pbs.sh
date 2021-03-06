#!/bin/bash
#PBS -N iqtree
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add iqtree-1.6.12

data_dir='/storage/brno3-cerit/home/kika/mic60-dynamins/ver2'

#copy files to scratch
cp $data_dir'/'*trimal*.aln $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

for f in *.aln ; do
 guide=guide_${f%.aln}
 guide_tree=$guide'.treefile'
 bb=1000
 iqtree -m LG+F+R8 -nt AUTO -ntmax $PBS_NUM_PPN -bb $bb -quiet -s ${f}
 # iqtree -m TEST -nt AUTO -ntmax $PBS_NUM_PPN -bb $bb -quiet -s ${f}
 # iqtree -m LG+F+G -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s ${f} -pre $guide
 # iqtree -m LG+C20+F+G -nt AUTO -ntmax $PBS_NUM_PPN -bb $bb -quiet -s ${f} -ft $guide_tree #-wsr
done

#copy files back
rm *.aln
cp * $data_dir
