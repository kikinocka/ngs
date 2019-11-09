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
cp $reads'all_r1_trimmed.fq.gz' $reads'all_r2_trimmed.fq.gz' $reads'all_unpaired.fq.gz' $SCRATCHDIR

assembly='contigs.fasta'
fw='all_r1_trimmed.fq.gz'
rv='all_r2_trimmed.fq.gz'
unpaired='all_unpaired.fq.gz'

base_name='EU17-18_bwa'
index_report='index_report.txt'
stat_mapped_paired=$base_name'_mapped_paired.flagstat'
bam_mapped_paired=$base_name'_mapped_paired.bam'
bai_mapped_paired=$base_name'_mapped_paired.bam.bai'
report_mapped_paired=$base_name'_mapped_paired.report.txt'
stat_mapped_unpaired=$base_name'_mapped_unpaired.flagstat'
bam_mapped_unpaired=$base_name'_mapped_unpaired.bam'
bai_mapped_unpaired=$base_name'_mapped_unpaired.bam.bai'
report_mapped_unpaired=$base_name'_mapped_unpaired.report.txt'
bam=$base_name'_mapped_all.bam'
sorted=$base_name'mapped_all.sorted.bam'


#compute on scratch
cd $SCRATCHDIR
bwa index -a bwtsw $assembly 2>$index_report

bwa mem -t $PBS_NUM_PPN $assembly $fw $rv | tee >(samtools flagstat - > $stat_mapped_paired) \
| samtools sort -O BAM | tee $bam_mapped_paired \
| samtools index - $bai_mapped_paired 2> $report_mapped_paired

bwa mem -t $PBS_NUM_PPN $assembly $unpaired | tee >(samtools flagstat - > $stat_mapped_unpaired) \
| samtools sort -O BAM | tee $bam_mapped_unpaired \
| samtools index - $bam_mapped_unpaired 2> report_mapped_unpaired

samtools merge -@ $PBS_NUM_PPN -f $bam $bam_mapped_paired $bam_mapped_unpaired
samtools sort -@ $PBS_NUM_PPN -o $sorted $bam
samtools index $sorted

#copy files back
rm $assembly $fw $rv $unpaired
cp * $outdir
