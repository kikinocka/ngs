#!/bin/env bash
slap_mapper='/home/nenarokova/tools/SLaPMapper/SLaPMapper.pl'
genome='/media/4TB1/blastocrithidia/genome_assembly/p57_scaffolds.fa'
reads1='/media/4TB1/blastocrithidia/reads/transcriptome/raw/p57_all_1.fastq.gz'
reads2='/media/4TB1/blastocrithidia/reads/transcriptome/raw/p57_all_2.fastq.gz'
gff='/media/4TB1/blastocrithidia/mapping/slap_mapping_both_libraries/empty_annotation.gff'
work_dir='/media/4TB1/blastocrithidia/mapping/slap_mapping_both_libraries/'

SL='AACGCATTTTTTGTTACAGTTTCTGTACTTTATTG'
min_length='6'

cd $work_dir
ln -s $reads1 reads1.fastq
ln -s $reads2 reads2.fastq
perl $slap_mapper -g $genome -l reads1.fastq -r reads2.fastq -a $gff -i $SL -s $min_length