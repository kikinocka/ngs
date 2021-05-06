#!/bin/bash
#PBS -N blast
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=3gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add maxbin-2.2.7

datadir='/storage/brno3-cerit/home/kika/oil_sands/metagenome/'

#copy files to scratch
cp $datadir'bml_meta.spades_def.fa' $SCRATCHDIR
cp $datadir'reads/BML_trimmed_1.fq.gz' $SCRATCHDIR
cp $datadir'reads/BML_trimmed_2.fq.gz' $SCRATCHDIR


#run on scratch
cd $SCRATCHDIR

meta='bml_meta.spades_def.fa'
fwd='BML_trimmed_1.fq.gz'
rev='BML_trimmed_2.fq.gz'
out='bml_meta.maxbin.out'

run_MaxBin.pl -contig $meta -reads $fwd -reads2 $rev -plotmarker -thread $PBS_NUM_PPN -out $out


#copy files back
rm $meta
cp -R * $datadir
