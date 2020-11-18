#!/bin/bash
#PBS -N blast
#PBS -l select=1:ncpus=15:mem=20gb:scratch_local=3gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blast+-2.8.0a

datadir='/storage/brno3-cerit/home/kika/bml/'

#copy files to scratch
cp $datadir'BML_photosystems_aa.fa' $SCRATCHDIR

query='BML_photosystems_aa.fa'
out='BML_photosystems.blast.xml'
db='/storage/projects/BlastDB/nr'
program=blastp
task=blastp
outfmt=5
eval=1
max_seqs=5

#run on scratch
cd $SCRATCHDIR

$program -task $task \
	-query $query \
	-db $db \
	-out $out \
	-outfmt $outfmt \
	-num_threads $PBS_NUM_PPN \
	-evalue $eval \
	-max_target_seqs $max_seqs \

#copy files back
rm $query
cp -R * $datadir
