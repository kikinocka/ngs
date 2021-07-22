#!/bin/bash
#PBS -N stampa
#PBS -l select=1:ncpus=15:mem=5gb:scratch_local=5gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add vsearch-1.4.4

data='/storage/brno3-cerit/home/kika/oil_sands/18S-V4-2018/'
scripts='/storage/brno2/home/kika/scripts/bash_scripts/metacentrum/amplicon_analysis/'

#copy files to scratch
cp $data'global_dereplicated_1f_representatives.fas' $SCRATCHDIR
cp $scripts'9b_stampa.sh' $SCRATCHDIR
cp $scripts'9c_stampa_merge.py' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

fasta='global_dereplicated_1f_representatives.fas'
stampa_sc='9b_stampa.sh'

./$stampa_sc $fasta SSU_V4

#copy files back
rm $fasta $stampa_sc '9c_stampa_merge.py'
cp -r * $data
