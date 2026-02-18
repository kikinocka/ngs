#!/bin/bash
#SBATCH --job-name=karect
#SBATCH --output=karect.%j.out
#SBATCH --error=karect.%j.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --time=02:00:00
#SBATCH --export=ALL

karect='/home/kika/tools/karect/karect'

cd '/home/kika/pkld/trimmed_all/'
# assembly='spades_75_karect/scaffolds.fasta'
fwd='Ag83_trimmed_1.fq'
rev='Ag83_trimmed_2.fq'
log='Ag83_karect_report.txt'
# fwd_kar='karect_eval/karect_triat_trimmed_75_1.fq'
# rev_kar='karect_eval/karect_triat_trimmed_75_2.fq'
# aln='reads/karect_eval/Btr_aln.txt'
# eval='reads/karect_eval/Btr_eval.txt'
# log_aln='reads/karect_eval/Btr.karect_aln.txt'
# log_eval='reads/karect_eval/Btr.karect_eval.txt'

$karect -correct -threads=10 -matchtype=hamming -celltype=diploid -inputfile=$fwd -inputfile=$rev 2> $log

# karect -align -threads=10 -matchtype=hamming \
#       -inputfile=/mnt/data/kika/blastocrithidia/b_triatomae/reads/triat_trimmed_75_1.fq \
#       -inputfile=/mnt/data/kika/blastocrithidia/b_triatomae/reads/triat_trimmed_75_2.fq \
#       -refgenomefile=/mnt/data/kika/blastocrithidia/b_triatomae/spades_75_karect/scaffolds.l500.fa \
#       -alignfile=/mnt/data/kika/blastocrithidia/b_triatomae/reads/karect_eval/Btr_aln.txt \
#       2> /mnt/data/kika/blastocrithidia/b_triatomae/reads/karect_eval/Btr.karect_aln.txt

# karect -eval -threads=10 -matchtype=hamming \
#       -inputfile=/mnt/data/kika/blastocrithidia/b_triatomae/reads/triat_trimmed_75_1.fq \
#       -inputfile=/mnt/data/kika/blastocrithidia/b_triatomae/reads/triat_trimmed_75_2.fq \
#       -resultfile=/mnt/data/kika/blastocrithidia/b_triatomae/reads/karect_triat_trimmed_75_1.fq \
#       -resultfile=/mnt/data/kika/blastocrithidia/b_triatomae/reads/karect_triat_trimmed_75_2.fq \
#       -refgenomefile=/mnt/data/kika/blastocrithidia/b_triatomae/spades_75_karect/scaffolds.l500.fa \
#       -alignfile=/mnt/data/kika/blastocrithidia/b_triatomae/reads/karect_eval/Btr_aln.txt \
#       -evalfile=/mnt/data/kika/blastocrithidia/b_triatomae/reads/karect_eval/Btr_eval.txt \ 
#       2> /mnt/data/kika/blastocrithidia/b_triatomae/reads/karect_eval/Btr.karect_eval.txt

python3 /home/kika/scripts/scripts/py_scripts/slackbot.py OSU: karect done
