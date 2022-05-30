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

datadir='/storage/brno3-cerit/home/kika/oil_sands/metagenomes/P1B_1-05C_L001-ds.ec8b691bd68b44deb59919ca3da275ba/'

#copy files to scratch
cp $datadir'2-spades/scaffolds.fasta' $SCRATCHDIR
cp $datadir'1-reads/P1B_all_trimmed_1.fq.gz' $SCRATCHDIR
cp $datadir'1-reads/P1B_all_trimmed_2.fq.gz' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

metagenome='scaffolds.fasta'
fwd='P1B_all_trimmed_1.fq.gz'
rev='P1B_all_trimmed_2.fq.gz'

metaquast.py -o $SCRATCHDIR -t $PBS_NUM_PPN -1 $fwd -2 $rev $metagenome


#copy results to your folder
rm $metagenome $fwd $rev
cp -r * $datadir'3-metaquast/'
