#!/bin/bash
#PBS -N TopHat2
#PBS -l select=1:ncpus=20:mem=50gb:scratch_local=50gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

#since tophat removes /1 and /2 from the read names, you need to modify the reads which you input to mark them 
#with -1 and -2 instead of /1 and /2

cat $PBS_NODEFILE

#add module
module add tophat-2.1.1
module add bowtie2-2.3.0
module add samtools-1.3.1

genome_dir='/storage/brno3-cerit/home/kika/pelomyxa/genome_assembly/'
reads='/storage/brno3-cerit/home/kika/pelomyxa/reads/transcriptome'
outdir='/storage/brno3-cerit/home/kika/pelomyxa/mapping/tophat2_genome_corr/'

#copy files to scratch
cp $genome_dir'pelomyxa_final_corr_genome.fa' $SCRATCHDIR
cp $reads'/'merged_trimmed_renamed* $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

genome='pelomyxa_final_corr_genome.fa'
index='pelomyxa_final_corr_bw2'
fwd='merged_trimmed_renamed_1.fq'
rv='merged_trimmed_renamed_2.fq'
report='pelomyxa_final_corr_tophat_report.txt'
out='tophat_out/'
bam=$out'accepted_hits.bam'
sam=$out'accepted_hits.sam'

bowtie2-build --threads $PBS_NUM_PPN $genome $index

tophat2 -r 50 --mate-std-dev 50 -i 30 -p $PBS_NUM_PPN -o $out $index $fwd $rv 2> $report

samtools view -bS $sam > $bam -@ $PBS_NUM_PPN
samtools index $bam

#copy files back
cd $out
cp -r * $outdir
