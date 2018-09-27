#!/bin/sh
#PBS -N FastQC
#PBS -l select=1:ncpus=4:mem=4gb:scratch_local=20gb
#PBS -l walltime=0:20:00

fastqc='/auto/brno2/home/kika/tools/miniconda3/pkgs/fastqc-0.11.7-5/bin/fastqc'
read_dir='/auto/brno3-cerit/nfs4/home/kika/pelomyxa/reads/genome/deep_hiseq/'
out_dir='/auto/brno3-cerit/nfs4/home/kika/pelomyxa/reads/genome/deep_hiseq/fastqc/'

fastqc -o $out_dir $read_dir'p1_r1.fastq.gz'
fastqc -o $out_dir $read_dir'p1_r2.fastq.gz'
