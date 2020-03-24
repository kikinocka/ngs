#!/bin/bash
#PBS -N Quast
#PBS -l select=1:ncpus=10:mem=3gb:scratch_local=100gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add quast-4.6.3

assembly='/storage/brno3-cerit/home/kika/kinetoplastids/lmex_genome/ku70/'
mapping=$assembly'bw2_mapping/pilon10/'
# outdir=$assembly'quast/'

#copy assembly to scratch
cp $assembly'ku70_pilon10.fa' $SCRATCHDIR
cp $mapping'ku70_p10_bw2_sorted.bam' $SCRATCHDIR

f='ku70_pilon10.fa'
bam='ku70_p10_bw2_sorted.bam'
output='quast/'
min_contig=500


#compute on scratch
cd $SCRATCHDIR
quast.py -o $output -t $PBS_NUM_PPN --glimmer --min-contig $min_contig --eukaryote --bam $bam $f

#copy results to your folder
rm $f $bam
cp -r * $assembly
