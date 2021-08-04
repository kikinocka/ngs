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

datadir='/storage/brno3-cerit/home/kika/oil_sands/metagenomes/P1-7m_1-07G_L001-ds.67bbce8fcfb6439db0445956cac4f716/'

#copy files to scratch
cp $datadir'spades/scaffolds.fasta' $SCRATCHDIR
cp $datadir'reads/P1-7_trimmed_1.fq.gz' $SCRATCHDIR
cp $datadir'reads/P1-7_trimmed_2.fq.gz' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

metagenome='scaffolds.fasta'
fwd='P1-7_trimmed_1.fq.gz'
rev='P1-7_trimmed_2.fq.gz'

metaquast.py -o $SCRATCHDIR -t $PBS_NUM_PPN -1 $fwd -2 $rev $metagenome


#copy results to your folder
rm $metagenome $fwd $rev
cp -r * $datadir'metaquast/'
