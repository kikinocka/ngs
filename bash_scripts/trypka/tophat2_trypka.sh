#!/bin/bash

bw2_dir='/home/kika/miniconda3/pkgs/bowtie2-2.3.4.2-py36h2d50403_0/bin/'
tophat='/home/nenarokova/tools/tophat-2.1.1.Linux_x86_64/tophat2'
diplo_dir='/media/4TB1/diplonema/'
mapping_dir=$diplo_dir'mapping/RNA_to_DNA/1604/'

genome=$diplo_dir'genome_assembly/1604/spades/scaffolds.fasta'
fw=$diplo_dir'reads/transcriptome/trimmed/1604_trimmed_1.fq.gz'
rv=$diplo_dir'reads/transcriptome/trimmed/1604_trimmed_2.fq.gz'
index=$mapping_dir'1604_bw2'
threads=30

$bw2_dir'bowtie2-build' --threads $threads $genome $index

#default parameters
$tophat -r 50 --mate-std-dev 20 -i 70 -p $threads -o $mapping_dir $index $fw $rv
