#!/bin/bash
#PBS -N pynast
#PBS -l select=1:ncpus=1:mem=20gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
# module add qiime-1.9.1
source /cvmfs/software.metacentrum.cz/modulefiles/5.1.0/loadmodules
module load qiime


data_dir='/storage/brno3-cerit/home/kika/sl_euglenozoa/v9/V9_DeepSea/euglenozoa/'

#copy files to scratch
cp $data_dir'euglenozoa.mafft.aln' $SCRATCHDIR
cp $data_dir'V9.fa' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

existing='euglenozoa.mafft.aln'
add='V9.fa'
aln='euglenozoa_V9.pynast.aln'
log='euglenozoa_V9.pynast.log'
# length=50

pynast -a $aln -g $log -i $add -t $existing
# -l $length 

#copy files back
rm $existing $add
cp * $data_dir
