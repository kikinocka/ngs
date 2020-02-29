#!/bin/bash
#PBS -N Bowtie2
#PBS -l select=1:ncpus=20:mem=50gb:scratch_local=50gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add bowtie2-2.3.0
module add samtools-1.3.1

data='/storage/brno3-cerit/home/kika/kinetoplastids/cfas_genome/'
outdir=$data'bw2_mapping/'

#copy files to scratch
cp $data'cfas_AODS02.fasta' $SCRATCHDIR
cp $data'reads/'*.fq.gz $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

base_name='cfas_bw2'
ref='cfas_AODS02.fasta'
p1_1='SRR1028161_trimmed_1.fq.gz'
p1_2='SRR1028161_trimmed_2.fq.gz'
p2_1='SRR1593518_trimmed_1.fq.gz'
p2_2='SRR1593518_trimmed_2.fq.gz'
p3_1='SRR834693_trimmed_1.fq.gz'
p3_2='SRR834693_trimmed_2.fq.gz'
samfile=$base_name'.sam'
unmapped_unpaired=$base_name'_unmapped_unpaired.fq'
unmapped_paired=$base_name'_unmapped_paired.fq'
report=$base_name'_report.txt'

bamfile=$base_name'_unsorted.bam'
sorted=$base_name'_sorted.bam'

bowtie2-build --threads $PBS_NUM_PPN $ref $base_name
bowtie2 --very-sensitive -p $PBS_NUM_PPN \
	-x $base_name \
	-1 $p1_1,$p2_1,$p3_1 \
	-2 $p1_2,$p2_2,$p3_2 \
	--un-gz $unmapped_unpaired \
	--un-conc-gz $unmapped_paired \
	-S $samfile 2> $report

samtools view -bS $samfile > $bamfile -@ $PBS_NUM_PPN
samtools sort -o $sorted -@ PBS_NUM_PPN $bamfile 
samtools index $sorted

#copy files back
cp *bw2* $outdir
