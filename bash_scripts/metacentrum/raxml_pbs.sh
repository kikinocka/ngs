#!/bin/bash
#PBS -N raxml-ACC
#PBS -l select=1:ncpus=10:mem=2gb:scratch_local=5gb
#PBS -l walltime=96:00:00
#PBS -m ae
#PBS -j oe
# previous lines defines: job name, queue where job run,
# resources that we request (finish in whoknows, tried 2 chains instead of 4, Ogar suggested)
# 25GB should be enough

DATADIR="/storage/brno3-cerit/home/fussyz01/VOB/glycine"
# add modules
module add raxml-8.2.4

# get name of machine where job is run
trap 'clean_scratch' TERM EXIT

cat $PBS_NODEFILE
cd $DATADIR
mkdir raxml
cp $DATADIR/*.fasta $SCRATCHDIR

cd $SCRATCHDIR

#alignment can be in fasta format
#-f E executes a very fast tree search, does not calculate branch lengths, similar to FastTree
for i in `ls *.fasta`;do 
	raxmlHPC-PTHREADS -T 10 -m PROTGAMMALG -p 12345 -# 5 -s $i -n ${i%%.*}-1
	raxmlHPC-PTHREADS -T 10 -m PROTGAMMALG -p 12345 -b 12345 -# 1000 -s $i -n ${i%%.*}-2
	raxmlHPC-PTHREADS -T 10 -m PROTGAMMALG -p 12345 -f b -t RAxML_bestTree.${i%%.*}-1 -z RAxML_bootstrap.${i%%.*}-2 -n ${i%%.*}-RXM.tre
	cp RAxML* $DATADIR/raxml
done

export CLEAN_SCRATCH=false
