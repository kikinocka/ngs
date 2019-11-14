#!/bin/bash
#PBS -N Quast
#PBS -l select=1:ncpus=10:mem=3gb:scratch_local=100gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add quast-4.6.3

assembly='/storage/brno3-cerit/home/kika/sags/reassembly/spades/'
mapping='/auto/brno3-cerit/nfs4/home/kika/sags/reassembly/mapping/bbmap/'
outdir='/storage/brno3-cerit/home/kika/sags/reassembly/reports/'

#copy assembly to scratch
cp $assembly'contigs.fasta' $SCRATCHDIR
cp $mapping'EU1718_bbm_mapped_all.sorted.bam' $SCRATCHDIR

f='contigs.fasta'
bam='EU1718_bbm_mapped_all.sorted.bam'
output='quast/'
min_contig=500


#compute on scratch
cd $SCRATCHDIR
quast.py -o $output -t PBS_NUM_PPN --glimmer --min-contig $min_contig --eukaryote --bam $bam $f

#copy results to your folder
rm $f $bam
cp -r * $outdir
