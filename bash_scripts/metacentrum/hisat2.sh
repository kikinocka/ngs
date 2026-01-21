#!/bin/bash
#PBS -N hisat2
#PBS -l select=1:ncpus=20:mem=70gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module load hisat2
module load samtools

genome_dir='/storage/brno12-cerit/home/kika/paratrimastix/'
read_dir='/storage/brno12-cerit/home/kika/paratrimastix/RNA_reads'
outdir='/storage/brno12-cerit/home/kika/paratrimastix/hisat2/illumina/'

#copy files to scratch
cp $genome_dir'PaPyr_JAPMOS01.fna' $SCRATCHDIR
cp $read_dir'/'*trimmed_*.fq.gz $SCRATCHDIR
# cp $outdir'/'* $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

genome='PaPyr_JAPMOS01.fna'
fw='SRR33713718_trimmed_1.fq.gz'
rv='SRR33713718_trimmed_2.fq.gz'
# sg='SRR651041_trimmed.fq.gz,SRR651098_trimmed.fq.gz'
index='PaPyr_ht2'
unmapped_unpaired=$index'_unmapped_unpaired.fq.gz'
unmapped_paired=$index'_unmapped_paired.fq.gz'
sam=$index'.sam'
report=$index'_report.txt'
bam=$index'_unsorted.bam'
sorted=$index'_sorted.bam'

hisat2-build -p $PBS_NUM_PPN $genome $index
hisat2 -p $PBS_NUM_PPN -x $index \
	--very-sensitive \
	--dta --secondary \
	-1 $fw \
	-2 $rv \
	--un-gz $unmapped_unpaired \
	--un-conc-gz $unmapped_paired \
	-S $sam 2> $report
#-U $sg \

samtools view -bS $sam > $bam -@ $PBS_NUM_PPN
samtools sort -o $sorted -@ $PBS_NUM_PPN $bam 
samtools index $sorted

#copy files back
rm $genome *.fq.gz
cp -r * $outdir
