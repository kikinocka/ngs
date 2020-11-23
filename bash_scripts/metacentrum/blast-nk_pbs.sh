#!/bin/bash
#PBS -N blast-nk
#PBS -l select=1:ncpus=15:mem=20gb:scratch_local=3gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blast+-2.8.0a

datadir='/storage/brno3-cerit/home/kika/trafficking/RABs/1621/'

#copy files to scratch
cp $datadir'fwd_hits.fa' $SCRATCHDIR

query='fwd_hits.fa'
out='rev_nr.blast.xml'
db='/storage/projects/BlastDB/nr'
program=blastx
task=blastx
outfmt=5
eval=1
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
