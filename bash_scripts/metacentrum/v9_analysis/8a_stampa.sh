#!/bin/bash
#PBS -N stampa
#PBS -l select=1:ncpus=15:mem=10gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add vsearch-1.4.4

data='/storage/brno3-cerit/home/kika/sl_euglenozoa/'
script='/storage/brno2/home/kika/scripts/kika/bash_scripts/metacentrum/v9_analysis/'

fasta=$data'global_dereplicated_1f_representatives.fas'
stampa_sc=$script'8b_stampa.sh'

#copy files to scratch
cp $fasta $SCRATCHDIR
cp $stampa_sc $SCRATCHDIR
cp $script'8c_stampa_merge.py' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

./$stampa_sc $fasta SSU_V9

#copy files back
rm $fasta $stampa_sc
cp -r * $data
