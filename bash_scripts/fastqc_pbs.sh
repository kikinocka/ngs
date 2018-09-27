#!/bin/sh
#PBS -N FastQC
#PBS -l select=1:ncpus=4:mem=4gb:scratch_local=10gb
#PBS -l walltime=1:00:00

fastqc='/auto/brno2/home/kika/tools/miniconda3/pkgs/fastqc-0.11.7-5/bin/fastqc'
read_dir='/media/4TB1/blastocrithidia/reads/transcriptome/trimmed/'
out_dir='/media/4TB1/blastocrithidia/reads/transcriptome/trimmed/fastqc/'

fastqc -o $out_dir $read_dir'p57_3-end_enriched_trimmed_1.fq.gz'
fastqc -o $out_dir $read_dir'p57_3-end_enriched_trimmed_2.fq.gz'
