#!/bin/bash
#PBS -N karect
#PBS -l nodes=1:ppn=10
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe


cd '/mnt/data/kika/blastocrithidia/b_triatomae/'
assembly='spades_75_karect/scaffolds.fasta'
fwd='reads/triat_trimmed_75_1.fq'
rev='reads/triat_trimmed_75_2.fq'
fwd_kar='karect_eval/karect_triat_trimmed_75_1.fq'
rev_kar='karect_eval/karect_triat_trimmed_75_2.fq'
aln='reads/karect_eval/Btr_aln.txt'
eval='reads/karect_eval/Btr_eval.txt'
log_aln='reads/karect_eval/Btr.karect_aln.txt'
log_eval='reads/karect_eval/Btr.karect_eval.txt'

# karect -correct -threads=10 -matchtype=hamming -celltype=diploid -inputfile=$fwd -inputfile=$rev 2> $log

karect -align -threads=10 -matchtype=hamming \
      -inputfile='/mnt/data/kika/blastocrithidia/b_triatomae/reads/triat_trimmed_75_1.fq' \
      -inputfile='/mnt/data/kika/blastocrithidia/b_triatomae/reads/triat_trimmed_75_2.fq' \
      -refgenomefile='/mnt/data/kika/blastocrithidia/b_triatomae/spades_75_karect/scaffolds.fasta' \
      -alignfile='/mnt/data/kika/blastocrithidia/b_triatomae/reads/karect_eval/Btr_aln.txt' \
      2> '/mnt/data/kika/blastocrithidia/b_triatomae/reads/karect_eval/Btr.karect_aln.txt'

karect -eval -threads=10 -matchtype=hamming \
      -inputfile='/mnt/data/kika/blastocrithidia/b_triatomae/reads/triat_trimmed_75_1.fq' \
      -inputfile='/mnt/data/kika/blastocrithidia/b_triatomae/reads/triat_trimmed_75_2.fq' \
      -resultfile='/mnt/data/kika/blastocrithidia/b_triatomae/reads/karect_triat_trimmed_75_1.fq' \
      -resultfile='/mnt/data/kika/blastocrithidia/b_triatomae/reads/karect_triat_trimmed_75_2.fq' \
      -refgenomefile='/mnt/data/kika/blastocrithidia/b_triatomae/spades_75_karect/scaffolds.fasta' \
      -alignfile='/mnt/data/kika/blastocrithidia/b_triatomae/reads/karect_eval/Btr_aln.txt' \
      -evalfile='/mnt/data/kika/blastocrithidia/b_triatomae/reads/karect_eval/Btr_eval.txt' \ 
      2> '/mnt/data/kika/blastocrithidia/b_triatomae/reads/karect_eval/Btr.karect_eval.txt'
