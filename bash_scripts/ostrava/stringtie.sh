#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N hisat2
#PBS -l nodes=1:ppn=20
#PBS -l walltime=50:00:00


cd '/mnt/data/kika/blastocrithidia/transcriptomes/b_raabei/'

stringtie='/home/users/kika/stringtie/stringtie'

$stringtie -v -o Wcollosoma_stringTie.gtf Wcol_af_correction.hisat2_sorted.bam -A gene_abundance_estimation.out.tsv -p 30