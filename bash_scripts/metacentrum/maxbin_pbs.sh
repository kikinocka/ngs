#!/bin/bash
#PBS -N maxbin
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
cp $datadir'reads/BML_trimmed_1.fa' $SCRATCHDIR
cp $datadir'reads/BML_trimmed_2.fa' $SCRATCHDIR


#run on scratch
cd $SCRATCHDIR

meta='bml_meta.spades_def.fa'
fwd='BML_trimmed_1.fa'
rev='BML_trimmed_2.fa'
out='bml_meta.maxbin.out'

run_MaxBin.pl -contig $meta -reads $fwd -reads2 $rev -plotmarker -thread $PBS_NUM_PPN -out $out


#copy files back
rm $meta $fwd $rev
cp -R * $datadir
