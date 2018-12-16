#!/bin/bash
#PBS -N Quast
#PBS -l select=1:ncpus=10:mem=3gb:scratch_local=100gb
#PBS -l walltime=00:10:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add quast-4.6.3

assembly='/auto/brno3-cerit/nfs4/home/kika/pelomyxa/genome_assembly/all_reads_k-mers/K33/'
outdir='/storage/brno3-cerit/home/kika/pelomyxa/genome_assembly/all_reads_k-mers/quast/k33/'

#copy assembly to scratch
cd $assembly
cp final_contigs.fasta $SCRATCHDIR

f='final_contigs.fasta'
output='k33/'

#compute on scratch
quast.py $f -o $output -t $PBS_NUM_PPN

#copy results to your folder
cd output
cp -R * $outdir
