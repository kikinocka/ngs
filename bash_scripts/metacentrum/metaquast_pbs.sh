#!/bin/bash
#PBS -N metaquast
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=20gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blast+-2.8.0a
module add quast-4.6.3

datadir='/storage/brno3-cerit/home/kika/oil_sands/metagenomes/P2S_1-01A_L001-ds.9f42a90caf694c0ab5686f0e22e79319/'

#copy files to scratch
cp $datadir'spades/scaffolds.fasta' $SCRATCHDIR
cp $datadir'reads/P2S_trimmed_1.fq.gz' $SCRATCHDIR
cp $datadir'reads/P2S_trimmed_1.fq.gz' $SCRATCHDIR

metagenome='scaffolds.fasta'
fwd='P2S_trimmed_1.fq.gz'
rev='P2S_trimmed_1.fq.gz'


#compute on scratch
cd $SCRATCHDIR
metaquast.py -o $SCRATCHDIR -t $PBS_NUM_PPN -1 $fwd -2 $rev $metagenome


#copy results to your folder
rm $metagenome $fwd $rev
cp -r * $datadir'metaquast/'
