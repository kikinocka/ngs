#!/bin/bash

mapper='/home/kika/tools/ContextMap_v2.7.9/ContextMap_v2.7.9.jar'
ref='/media/4TB1/blastocrithidia/genome_assembly/bnonstop_corrected_assembly.fasta'
split_genome='/media/4TB1/blastocrithidia/new_3-UTR/contextmap/Bn_split_genome/'

read_dir='/media/4TB1/blastocrithidia/new_3-UTR/trimmed_RNA_reads/'
p1_1=$read_dir'p57_3-end_trimmed_1.fq.gz'
p1_2=$read_dir'p57_3-end_trimmed_2.fq.gz'


cd '/media/4TB1/blastocrithidia/new_3-UTR/contextmap/'
base_name='p57_3-end_cm'
bw2_path='/home/kika/miniconda3/bin/bowtie2'
bw2i_path='/home/kika/miniconda3/bin/bowtie2-build'

# bowtie2-build --threads 30 $ref $base_name

java -jar $mapper mapper \
	-reads $p1_1,$p1_2 \
	-aligner_name bowtie2 \
	-aligner_bin $bw2_path \
	-indexer_bin $bw2i_path \
	-indices 'p57_3-end_cm.1.bt2','p57_3-end_cm.2.bt2','p57_3-end_cm.3.bt2','p57_3-end_cm.4.bt2','p57_3-end_cm.rev.1.bt2','p57_3-end_cm.rev.2.bt2' \
	-genome $split_genome \
	-o '/media/4TB1/blastocrithidia/new_3-UTR/contextmap/'
