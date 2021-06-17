#!/bin/bash
#PBS -N stampa
#PBS -l select=1:ncpus=15:mem=1gb:scratch_local=5gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add vsearch-1.4.4

data='/storage/brno3-cerit/home/kika/oil_sands/Lane26_18S_V9/'
script='/storage/brno2/home/kika/scripts/kika/bash_scripts/metacentrum/v9_analysis/'

#copy files to scratch
cp $data'global_dereplicated_1f_representatives.fas' $SCRATCHDIR
cp $script'9b_stampa.sh' $SCRATCHDIR
cp $script'9c_stampa_merge.py' $SCRATCHDIR

fasta='global_dereplicated_1f_representatives.fas'
stampa_sc='9b_stampa.sh'


#compute on scratch
cd $SCRATCHDIR

./$stampa_sc $fasta SSU_V9

#copy files back
rm $fasta $stampa_sc '9c_stampa_merge.py'
cp -r * $data
