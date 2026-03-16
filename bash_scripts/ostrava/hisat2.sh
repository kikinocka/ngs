#!/bin/bash
#SBATCH --job-name=hisat2
#SBATCH --output=hisat2.%j.out
#SBATCH --error=hisat2.%j.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=50
#SBATCH --time=02:00:00
#SBATCH --export=ALL

cd '/home/kika/tboissoni/'

genome='Tboi_masked.fna'
# fw='Tboi_trimmed50_1.fq.gz'
# rv='Tboi_trimmed50_2.fq.gz'
base_name='Tboi_ht2'
# unmapped_unpaired=$base_name'_unmapped_unpaired.fq.gz'
# unmapped_paired=$base_name'_unmapped_paired.fq.gz'
# sam=$base_name'.sam'
# report=$base_name'_report.txt'
# bam=$base_name'_unsorted.bam'
sorted=$base_name'_sorted.bam'
view_report=$base_name'.view.txt'

# hisat2-build -p 50 $genome $base_name
# hisat2 -p 50 \
# 	--very-sensitive \
# 	--dta --secondary \
# 	-x $base_name \
# 	-1 $fw \
# 	-2 $rv \
# 	--un-gz $unmapped_unpaired \
# 	--un-conc-gz $unmapped_paired \
# 	-S $sam 2> $report
# #--dta 			reports alignments tailored for transcript assemblers
# #--secondary	reports secondary alignments

# # samtools view -bS -F 4 $sam > $bam -@ 20 #writes only mapped reads to bamfile
# samtools view -bS -@ 50 $sam > $bam
# samtools sort -o $sorted -@ 50 $bam 
# samtools index $sorted

samtools tview --reference $genome $sorted > $view_report
