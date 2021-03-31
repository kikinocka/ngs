#!/bin/bash
#PBS -N metaquast
#PBS -l select=1:ncpus=15:mem=5gb:scratch_local=10gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blast+-2.8.0a
module add quast-4.6.3

datadir='/storage/brno3-cerit/home/kika/oil_sands/metagenome/'

#copy files to scratch
cp $datadir'spades_assembly/scaffolds.fasta' $SCRATCHDIR
cp $datadir'reads/BML_trimmed_1.fq.gz' $SCRATCHDIR
cp $datadir'reads/BML_trimmed_2.fq.gz' $SCRATCHDIR

assemblies='scaffolds.fasta'
fwd='BML_trimmed_1.fq.gz'
rev='BML_trimmed_2.fq.gz'
blast='/storage/projects/BlastDB/nt'


#compute on scratch
cd $SCRATCHDIR
metaquast.py -o $SCRATCHDIR -t $PBS_NUM_PPN -1 $fwd -2 $rev --blast-db $blast $assemblies


#copy results to your folder
rm $assemblies $fwd $rev
cp -r * $datadir'quast/'
