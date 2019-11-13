#!/bin/sh
#PBS -N bbmap
#PBS -l select=1:ncpus=20:mem=10gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add bbmap-36.92
module add samtools-1.3.1

sags='/storage/brno3-cerit/home/kika/sags/reassembly/'
reads=$sags'trimmed_reads/'
spades=$sags'spades/'
outdir=$sags'mapping/bbmap/'

#copy files to scratch
cp $spades'contigs.fasta' $SCRATCHDIR
cp $reads'all_r1_trimmed.fq.gz' $reads'all_r2_trimmed.fq.gz' $reads'all_unpaired.fq.gz' $SCRATCHDIR

assembly='contigs.fasta'
fw='all_r1_trimmed.fq.gz'
rv='all_r2_trimmed.fq.gz'
unpaired='all_unpaired.fq.gz'

base_name='EU1718_bbm_'
sam_mapped_paired=$base_name'mapped_paired.sam'
bam_mapped_paired=$base_name'mapped_paired.bam'
sorted_mapped_paired=$base_name'mapped_paired.sorted.bam'
stat_mapped_paired=$base_name'mapped_paired.flagstat'
report_mapped_paired=$base_name'mapped_paired.report'

sam_mapped_unpaired=$base_name'mapped_unpaired.sam'
bam_mapped_unpaired=$base_name'mapped_unpaired.bam'
sorted_mapped_unpaired=$base_name'mapped_unpaired.sorted.bam'
stat_mapped_unpaired=$base_name'mapped_unpaired.flagstat'
report_mapped_unpaired=$base_name'mapped_unpaired.report'

bam=$base_name'mapped_all.bam'
sorted=$base_name'mapped_all.sorted.bam'


#compute on scratch
cd $SCRATCHDIR
$bbmap.sh in=$fw in2=$rv out=$sam_mapped_paired ref=$assembly threads=$PBS_NUM_PPN 2> $report_mapped_paired
samtools view -bS $sam_mapped_paired > $bam_mapped_paired -@ $PBS_NUM_PPN
samtools flagstat $bam_mapped_paired > $stat_mapped_paired
samtools sort -o $sorted_mapped_paired -@ PBS_NUM_PPN $bam_mapped_paired
samtools index $sorted_mapped_paired

$bbmap.sh in=$unpaired out=$sam_mapped_unpaired ref=$assembly threads=$PBS_NUM_PPN 2> $report_mapped_unpaired
samtools view -bS $sam_mapped_unpaired > $bam_mapped_unpaired -@ $PBS_NUM_PPN
samtools flagstat $bam_mapped_unpaired > $stat_mapped_unpaired
samtools sort -o $sorted_mapped_unpaired -@ PBS_NUM_PPN $bam_mapped_unpaired
samtools index $sorted_mapped_unpaired

samtools merge -@ $PBS_NUM_PPN -f $bam $sorted_mapped_paired $sorted_mapped_unpaired
samtools sort -@ $PBS_NUM_PPN -o $sorted $bam
samtools index $sorted

#copy files back
rm $assembly $fw $rv $unpaired
cp -r * $outdir
