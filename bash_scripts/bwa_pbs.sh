#!/bin/bash
#PBS -N bwa
#PBS -l select=1:ncpus=25:mem=50gb:scratch_local=100gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add bwa-0.7.3a
module add samtools-1.3.1

sags='/storage/brno3-cerit/home/kika/sags/reassembly/'
reads=$sags'trimmed_reads/'
spades=$sags'spades/'
outdir=$sags'mapping_bwa/'

#copy files to scratch
cp $spades'contigs.fasta' $SCRATCHDIR
# cp $reads'all_r1_trimmed.fq.gz' $reads'all_r2_trimmed.fq.gz' $reads'all_unpaired.fq.gz' $SCRATCHDIR
cp $outdir'EU1718_bwa_mapped_paired.sam' $outdir'EU1718_bwa_mapped_unpaired.sam' $SCRATCHDIR

assembly='contigs.fasta'
# fw='all_r1_trimmed.fq.gz'
# rv='all_r2_trimmed.fq.gz'
# unpaired='all_unpaired.fq.gz'

base_name='EU1718_bwa_'
index_report=$base_name'index_genome.report'
stat_mapped_paired=$base_name'mapped_paired.flagstat'
sam_mapped_paired=$base_name'mapped_paired.sam'
bam_mapped_paired=$base_name'mapped_paired.bam'
sorted_mapped_paired=$base_name'mapped_paired.sorted.bam'
# bai_mapped_paired=$base_name'mapped_paired.sorted.bam.bai'
# report_mapped_paired=$base_name'mapped_paired.report'
stat_mapped_unpaired=$base_name'mapped_unpaired.flagstat'
sam_mapped_unpaired=$base_name'mapped_unpaired.sam'
bam_mapped_unpaired=$base_name'mapped_unpaired.bam'
sorted_mapped_unpaired=$base_name'mapped_unpaired.sorted.bam'
# bai_mapped_unpaired=$base_name'mapped_unpaired.bam.bai'
# report_mapped_unpaired=$base_name'mapped_unpaired.report'
bam=$base_name'mapped_all.bam'
sorted=$base_name'mapped_all.sorted.bam'


#compute on scratch
cd $SCRATCHDIR
bwa index -a bwtsw $assembly 2>$index_report

# bwa mem -t $PBS_NUM_PPN $assembly $fw $rv > $sam_mapped_paired 2> $report_mapped_paired
samtools view -bS $sam_mapped_paired > $bam_mapped_paired -@ $PBS_NUM_PPN
samtools flagstat $bam_mapped_paired > $stat_mapped_paired
samtools sort -O BAM -o $sorted_mapped_paired -@ PBS_NUM_PPN $bam_mapped_paired
samtools index $sorted_mapped_paired

# bwa mem -t $PBS_NUM_PPN $assembly $unpaired > $sam_mapped_unpaired 2> $report_mapped_unpaired
samtools view -bS $sam_mapped_unpaired > $bam_mapped_unpaired -@ $PBS_NUM_PPN
samtools flagstat $bam_mapped_unpaired > $stat_mapped_unpaired
samtools sort -O BAM -o $sorted_mapped_unpaired -@ PBS_NUM_PPN $bam_mapped_unpaired
samtools index $sorted_mapped_unpaired

samtools merge -@ $PBS_NUM_PPN -f $bam $sorted_mapped_paired $sorted_mapped_unpaired
samtools sort -@ $PBS_NUM_PPN -o $sorted $bam
samtools index $sorted

#copy files back
rm $assembly $sam_mapped_unpaired $sam_mapped_unpaired #$fw $rv $unpaired
cp * $outdir
