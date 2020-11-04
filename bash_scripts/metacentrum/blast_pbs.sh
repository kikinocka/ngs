#!/bin/bash
#PBS -N blast
#PBS -l select=1:ncpus=15:mem=20gb:scratch_local=3gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blast+-2.8.0a

datadir='/storage/brno3-cerit/home/kika/trafficking/RABs/dpap/'

#copy files to scratch
cp $datadir'1608_fwd_hits.fa' $SCRATCHDIR

query='fwd_hits.fa'
out='rev_nr.blast.xml'
db='/storage/projects/BlastDB/nr'
program=blastp
task=blastp
outfmt=5
eval=1e-04
max_seqs=1

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
