#!/bin/bash
#PBS -N hisat2
#PBS -l select=1:ncpus=20:mem=50gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
# module load hisat2
module load samtools

genome_dir='/storage/brno12-cerit/home/kika/trypanosoma_boissoni/'
# read_dir='/storage/brno12-cerit/home/kika/trypanosoma_boissoni/RNA_reads'
outdir='/storage/brno12-cerit/home/kika/trypanosoma_boissoni//hisat2/'

#copy files to scratch
cp $genome_dir'Tboi_masked.fna' $SCRATCHDIR
# cp $read_dir'/'*trimmed50* $SCRATCHDIR
cp $outdir'Tboi_ht2_sorted.bam'* $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

genome='Tboi_masked.fna'
# fw='Tboi_trimmed50_1.fq.gz'
# rv='Tboi_trimmed50_1.fq.gz'
# # sg='SRR651041_trimmed.fq.gz,SRR651098_trimmed.fq.gz'
index='Tboi_ht2'
# unmapped_unpaired=$index'_unmapped_unpaired.fq.gz'
# unmapped_paired=$index'_unmapped_paired.fq.gz'
# sam=$index'.sam'
# report=$index'_report.txt'
# bam=$index'_unsorted.bam'
sorted=$index'_sorted.bam'
view_report=$index'.view.txt '

# hisat2-build -p $PBS_NUM_PPN $genome $index
# hisat2 -p $PBS_NUM_PPN -x $index \
# 	--very-sensitive \
# 	--dta --secondary \
# 	-1 $fw \
# 	-2 $rv \
# 	--un-gz $unmapped_unpaired \
# 	--un-conc-gz $unmapped_paired \
# 	-S $sam 2> $report
# #-U $sg \

# samtools view -bS $sam > $bam -@ $PBS_NUM_PPN
# samtools sort -o $sorted -@ $PBS_NUM_PPN $bam 
# samtools index $sorted

samtools tview --reference $genome $sorted > $view_report

#copy files back
# rm $genome *.fq.gz
rm $genome $sorted
cp -r * $outdir
