#!/bin/bash
#PBS -N Hisat2
#PBS -l select=1:ncpus=20:mem=70gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add hisat2-2.0.5
module add samtools-1.3.1


genome_dir='/storage/brno3-cerit/home/kika/pelomyxa/genome_assembly/'
reads='/storage/brno3-cerit/home/kika/pelomyxa/reads/transcriptome/'
outdir='/storage/brno3-cerit/home/kika/pelomyxa/mapping/hisat2_genome_corr/'

#copy files to scratch
cp $genome_dir'pelomyxa_final_corr_genome.fa' $SCRATCHDIR
cp $reads'merged_trimmed_1.fq' $reads'merged_trimmed_2.fq' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

genome='pelomyxa_final_corr_genome.fa'
fw='merged_trimmed_1.fq'
rv='merged_trimmed_2.fq'
index='pelomyxa_final_corr_ht2'
unmapped_unpaired=$index'_unmapped_unpaired.fq.gz'
unmapped_paired=$index'_unmapped_paired.fq.gz'
sam=$index'.sam'
report=$index'_report.txt'
bam=$index'_unsorted.bam'
sorted=$index'_sorted.bam'

hisat2-build -p $PBS_NUM_PPN $genome $index
hisat2 -p $PBS_NUM_PPN -x $index -1 $fw -2 $rv --un-gz $unmapped_unpaired --un-conc-gz $unmapped_paired -S $sam 2> $report

samtools view -bS $sam > $bam -@ $PBS_NUM_PPN
samtools sort -o $sorted -@ PBS_NUM_PPN $bam 
samtools index $sorted

#copy files back
rm $genome $fw $rv
cp -r * $outdir
