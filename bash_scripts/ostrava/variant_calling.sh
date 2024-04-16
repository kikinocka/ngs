#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N variant_calling
#PBS -l nodes=1:ppn=40
#PBS -l walltime=100:00:00

base='Omod'
genome_dir='/mnt/data/kika/blastocrithidia/genomes/final_assemblies/'
genome=$genome_dir$base'_genome_final_masked.fa'
genome_dict=$genome_dir$base'_genome_final_masked.dict'
bam_dir='/mnt/data/kika/blastocrithidia/genomes/o_modryi/bowtie2/final/'
sorted_bam=$bam_dir$base'_bw2_sorted.bam'
removed_dupl_bam=$bam_dir$base'_bw2_sorted.dupl_removed.bam'
removed_dupl_log=$bam_dir$base'_bw2_sorted.dupl_removed_log.txt'
groups_bam=$bam_dir$base'_bw2_sorted.dupl_removed.read_groups.bam'
indels=$bam_dir$base'_only_indels.vcf'
indels_sorted=$bam_dir$base'_only_indels.sorted.vcf'
intervals=$bam_dir$base'_forIndelRealigner.intervals'
final_bam=$bam_dir$base'_bw2_sorted.dupl_removed.read_groups.IndelRealigner.bam'

#1st
eval "$(/home/users/bio/anaconda3/bin/conda shell.bash hook)"
# gatk MarkDuplicates -I $sorted_bam -O $removed_dupl_bam -M $removed_dupl_log \
# 	--REMOVE_DUPLICATES true --MAX_RECORDS_IN_RAM 100000000 --MAX_FILE_HANDLES_FOR_READ_ENDS_MAP 1000

# #2nd
# samtools index $removed_dupl_bam -@ 10
# samtools faidx $genome

# #3rd
# eval "$(/home/users/kika/miniconda3/bin/conda shell.bash hook)"
# conda activate platypus
# platypus callVariants --bamFiles=$removed_dupl_bam --refFile=$genome --output=$indels --minReads 3 --genSNPs 0 --genIndels 1 --nCPU 40
# conda deactivate

# #4th
# eval "$(/home/users/bio/anaconda3/bin/conda shell.bash hook)"
# gatk CreateSequenceDictionary -R $genome -O $genome_dict

# #5th
# gatk AddOrReplaceReadGroups -I $removed_dupl_bam -O $groups_bam -RGID 4 -RGLB lib1 -RGPL illumina -RGPU unit1 -RGSM 20

# #6th
# eval "$(/home/users/kika/miniconda3/bin/conda shell.bash hook)"
# conda activate bowtie2
# samtools index $groups_bam -@ 10
# conda deactivate

# #7th
# eval "$(/home/users/bio/anaconda3/bin/conda shell.bash hook)"
# gatk SortVcf -I $indels -O $indels_sorted --SEQUENCE_DICTIONARY $genome_dict

# #8th
# java -jar /home/users/bio/anaconda3/opt/gatk-3.8/GenomeAnalysisTK.jar -T RealignerTargetCreator \
# 	-R $genome -I $groups_bam --known $indels_sorted -o $intervals -nt 25

#9th
java -jar /home/users/bio/anaconda3/opt/gatk-3.8/GenomeAnalysisTK.jar -T IndelRealigner \
	-R $genome -I $groups_bam -known $indels_sorted --targetIntervals $intervals -o $final_bam


python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: variant calling done
