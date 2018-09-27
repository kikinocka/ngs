#!/bin/bash
#PBS -N BBduk
#PBS -l select=1:ncpus=4:mem=4gb:scratch_local=10gb
#PBS -l walltime=1:00:00

bbduk='/auto/brno2/home/kika/tools/bbmap/bbduk.sh'
read_dir='/media/4TB1/blastocrithidia/reads/transcriptome/raw/'
fw=$read_dir'p57_3-end_enriched_1.fastq.gz'
rv=$read_dir'p57_3-end_enriched_2.fastq.gz'
trimdir='/media/4TB1/blastocrithidia/reads/transcriptome/trimmed/'
name='p57_3-end_enriched'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'

bbduk overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t qtrim=rl trimq=20 ktrim=r k=22 mink=11 hdist=2 tpe tbo t=30
