#!/bin/sh
#PBS -N cd-hit
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=5gb
#PBS -l walltime=04:00:00
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
window=10

cd-hit-est -i $db -o $out -c $threshold -n $window -d 0 -M 20000 -T $PBS_NUM_PPN


#copy files back
rm $db
cp -R * $data
