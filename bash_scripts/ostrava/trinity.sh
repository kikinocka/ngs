#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N Trinity
#PBS -l nodes=1:ppn=30
#PBS -l walltime=100:00:00


cd '/home/users/kika/schizosaccharomyces_japonicus/'

read_dir='reads/'
out_dir='donna8_trinity'

fw=$read_dir'NG-A0875_Donna_8_trimmed_1.fq.gz'
rv=$read_dir'NG-A0875_Donna_8_trimmed_2.fq.gz'


eval "$(/home/users/kika/miniconda3/bin/conda shell.bash hook)"
conda activate trinity

Trinity --seqType fq --left $fw --right $rv --output $out_dir --max_memory 50G --CPU 30

conda deactivate

mv donna8_trinity.Trinity.fasta donna8.Trinity.fasta
mv donna8_trinity.Trinity.fasta.gene_trans_map donna8.Trinity.fasta.gene_trans_map
mv donna8.Trinity.fasta* $out_dir


python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: Trinity done
