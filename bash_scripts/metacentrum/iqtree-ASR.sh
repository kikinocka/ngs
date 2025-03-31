#!/bin/bash
#PBS -N IQT-ASR
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module load iqtree

data_dir='/storage/brno12-cerit/home/kika/trafficking/clathrin/ver5/'

#copy files to scratch
cp $data_dir'CHC_opisthokonta.man_trim.CD.aln' $SCRATCHDIR
cp $data_dir'asr/CHC_opisthokonta.man_trim.CD.rooted.treefile' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

aln='CHC_opisthokonta.man_trim.CD.aln'
tree='CHC_opisthokonta.man_trim.CD.rooted.treefile'

iqtree -m LG+C40+G+F+R5 -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s $aln -te $tree -asr


#copy files back
rm *.aln *rooted.treefile
cp * $data_dir
