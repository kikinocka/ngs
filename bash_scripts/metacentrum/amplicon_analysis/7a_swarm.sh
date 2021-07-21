#!/bin/bash
#PBS -N swarm
#PBS -l select=1:ncpus=15:mem=1gb:scratch_local=5gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add swarm-3.0.0

data='/storage/brno3-cerit/home/kika/oil_sands/18S-V4-2018/'
scripts='/storage/brno2/home/kika/scripts/bash_scripts/metacentrum/amplicon_analysis/'

#copy files to scratch
cp $data'global_dereplicated.fa' $SCRATCHDIR
cp $scripts'7b_swarm_fastidious.sh' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR
# if [ $# != 1 ]; then
#     echo 'You need to supply an input filename - this is your global dereplicated fasta file (not the bzip)!';
#     exit 1;
# fi
touch 'global_dereplicated_1f.swarms' 'global_dereplicated_1f.stats' 'global_dereplicated_1f_representatives.fas'

fasta='global_dereplicated.fa'
swarm_sc='7b_swarm_fastidious.sh'

./$swarm_sc $fasta

#copy files back
rm $fasta $swarm_sc
cp * $data
