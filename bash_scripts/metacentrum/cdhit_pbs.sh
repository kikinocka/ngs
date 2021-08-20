#!/bin/sh
#PBS -N cd-hit
#PBS -l select=1:ncpus=10:mem=10gb:scratch_local=3gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add cdhit-4.6.1

data='/storage/brno3-cerit/home/kika/databases/pr2db/4.14.0/'

#copy files to scratch
cp $data'pr2_version_4.14.0_SSU_UTAX.fasta' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

db='pr2_version_4.14.0_SSU_UTAX.fasta'
out='pr2_version_4.14.0_SSU_UTAX.cdhit98.fasta'
threshold=0.98
window=11

cd-hit-est -i $db -o $out -c $threshold -n $window -d 0 -M 10000 -T $PBS_NUM_PPN
# -c	sequence identity threshold, default 0.9
# -n	word_length, default 10, see user's guide for choosing it
# -d	length of description in .clstr file, default 20
# -M	memory limit (in MB) for the program, default 800; 0 for unlimitted;


#copy files back
rm $db
cp -R * $data
