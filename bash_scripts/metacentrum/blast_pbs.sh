#!/bin/bash
#PBS -N blast
#PBS -l select=1:ncpus=10:mem=20gb:scratch_local=3gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blast+-2.8.0a

datadir='/storage/brno3-cerit/home/kika/trafficking/RABs/1608/'

#copy files to scratch
cp $datadir'1608_fwd_hits.fa' $SCRATCHDIR

query='1608_fwd_hits.fa'
out='1608.rev_nr.blast.xml'
# db=$datadir'genome_db/pzop_genome.fa'
db='/storage/projects/BlastDB/nr'
program=blastx
task=blastx
outfmt=5
eval=0.0001
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
