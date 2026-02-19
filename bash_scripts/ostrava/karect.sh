#!/bin/bash
#SBATCH --job-name=karect
#SBATCH --output=karect.%j.out
#SBATCH --error=karect.%j.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --time=10:00:00
#SBATCH --export=ALL

karect='/home/kika/tools/karect/karect'

cd '/home/kika/pkld/trimmed_75/'

for file in *_1.fq ; do 
      name=${file%_*.fq}
      fwd=$name'_1.fq'
      rev=$name'_2.fq'
      log=$name'_karect_report.txt'
      echo $name
      $karect -correct -threads=10 -matchtype=hamming -celltype=diploid -inputfile=$fwd -inputfile=$rev 2> $log
done

# assembly='spades_75_karect/scaffolds.fasta'
# fwd_kar='karect_eval/karect_triat_trimmed_75_1.fq'
# rev_kar='karect_eval/karect_triat_trimmed_75_2.fq'
# aln='reads/karect_eval/Btr_aln.txt'
# eval='reads/karect_eval/Btr_eval.txt'
# log_aln='reads/karect_eval/Btr.karect_aln.txt'
# log_eval='reads/karect_eval/Btr.karect_eval.txt'

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
