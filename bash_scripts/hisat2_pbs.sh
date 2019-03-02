#!/bin/bash
#PBS -N HISAT2
#PBS -l select=1:ncpus=15:mem=20gb:scratch_local=100gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add hisat2-2.0.5
module add samtools-1.3.1

#copy files to scratch
cd /storage/brno3-cerit/home/kika/pelomyxa/genome_assembly/clean/
cp pelomyxa_clean.fa $SCRATCHDIR/pelo_clean_merged_ht2.fa

cd /storage/brno3-cerit/home/kika/pelomyxa/reads/transcriptome/
cp merged_trimmed* $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

genome='pelo_clean_merged_ht2.fa'
index='pelo_clean_merged_ht2'
fwd='merged_trimmed_1.fq.gz'
rv='merged_trimmed_2.fq.gz'
unmapped_unpaired=$index'_unmapped_unpaired.fq'
unmapped_paired=$index'_unmapped_paired.fq'
sam=$index'.sam'
report=$index'.txt'
bam=$index'_unsorted.bam'
sorted=$index'_sorted.bam'

hisat2-build -p $PBS_NUM_PPN $genome $index
hisat2 -p $PBS_NUM_PPN -x $index -1 $fwd -2 $rv --un-gz $unmapped_unpaired --un-conc-gz $unmapped_paired -S $sam 2> $report

samtools view -bS $sam > $bam -@ $PBS_NUM_PPN
samtools sort -o $sorted -@ PBS_NUM_PPN $bam 
samtools index $sorted

#copy files back
rm $genome $fwd $rv
cp -r * /storage/brno3-cerit/home/kika/pelomyxa/mapping/hisat2/.
