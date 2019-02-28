#!/bin/bash
#PBS -N TopHat2
#PBS -l select=1:ncpus=30:mem=50gb:scratch_local=100gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add tophat-2.1.1
module add bowtie2-2.3.0
module add samtools-1.3.1

#copy files to scratch
cd /storage/brno3-cerit/home/kika/pelomyxa/genome_assembly/clean/
cp pelomyxa_clean.fa $SCRATCHDIR/pelo_clean_merged_bw2.fa

cd /storage/brno3-cerit/home/kika/pelomyxa/reads/transcriptome/
cp merged_trimmed* $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

genome='pelo_clean_merged_bw2.fa'
index='pelo_clean_merged_bw2'
fwd='merged_trimmed_1.fq.gz'
rv='merged_trimmed_2.fq.gz'
out='tophat_out'

bowtie2-build --threads $PBS_NUM_PPN $genome $index

tophat2 -r 50 --mate-std-dev 50 -p $PBS_NUM_PPN -o $out $index $fwd $rv

#copy files back
cd $out
cp * /storage/brno3-cerit//home/kika/pelomyxa/mapping/tophat2/.
