#!/bin/bash
#PBS -N swarm
#PBS -l select=1:ncpus=15:mem=10gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add swarm-3.0.0

data='/storage/brno3-cerit/home/kika/sl_euglenozoa/'
script='/storage/brno2/home/kika/scripts/kika/bash_scripts/metacentrum/v9_analysis/'

#copy files to scratch
cp $data'global_dereplicated.fa' $SCRATCHDIR
cp $script'7b_swarm_fastidious.sh' $SCRATCHDIR

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
