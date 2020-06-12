#!/bin/bash
#PBS -N IQT-mitEbs
#PBS -q default
#PBS -l select=1:ncpus=10:mem=10gb:scratch_local=1gb:os=debian9
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add iqtree-1.6.8

datadir='/storage/brno3-cerit/home/kika/sags/mit/ver5_eug_bs/'

#copy files to scratch
cp $datadir'mit_eug_concat.aln' $SCRATCHDIR
# cp $datadir'guide_acsl_seqs.treefile' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR
aln='mit_eug_concat.aln'
# guide='guide_nifU'
# guide_tree=$guide'.treefile'
bb=1000

iqtree -s $aln -b $bb -nt AUTO -ntmax $PBS_NUM_PPN -m TEST -quiet -wsr
# iqtree -s $aln -b $bb -nt AUTO -ntmax $PBS_NUM_PPN -m GTR+G -quiet

# iqtree -m LG+F+G -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s $aln -pre $guide
# iqtree -m LG+C20+F+G -nt AUTO -ntmax $PBS_NUM_PPN -bb $bb -quiet -s $aln -ft $guide_tree #-wsr

#copy files back
rm $aln
cp * $datadir
