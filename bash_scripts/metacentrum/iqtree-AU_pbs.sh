#!/bin/bash
#PBS -N IQT-AU
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add iqtree-2.2.0

datadir='/storage/brno3-cerit/home/kika/trafficking/diplonemids_COPII/ver7/sec13_AU/ver3/'

#copy files to scratch
cp $datadir'sec13.trimal_gt-0.8.aln' $SCRATCHDIR
cp $datadir'sec13_topologies.trees' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR
aln='sec13.trimal_gt-0.8.aln'
trees='sec13_topologies.trees'

iqtree2 -m LG4X -nt AUTO -ntmax $PBS_NUM_PPN --test-weight --test-au --test 10000 -n 100 -s $aln --trees $trees

#copy files back
rm $aln
cp * $datadir
