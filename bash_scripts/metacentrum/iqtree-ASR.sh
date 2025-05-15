#!/bin/bash
#PBS -N IQT-ASR
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module load iqtree

data_dir='/storage/brno12-cerit/home/kika/trafficking/clathrin/CLC/ver2/'

#copy files to scratch
cp $data_dir'CLC_opisthokonta.man_trim.aln' $SCRATCHDIR
cp $data_dir'ASR/CLC_opisthokonta.man_trim.rooted.treefile' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

aln='CLC_opisthokonta.man_trim.aln'
tree='CLC_opisthokonta.man_trim.rooted.treefile'

iqtree -m LG4M+F+R4 -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s $aln -te $tree -asr


#copy files back
rm *.aln *rooted.treefile
cp * $data_dir'ASR'
