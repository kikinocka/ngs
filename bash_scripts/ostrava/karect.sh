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
      -inputfile=$fwd \
      -inputfile=$rev \
      -refgenomefile=$assembly \
      -alignfile=$aln 2> $log_aln

karect -eval -threads=10 -matchtype=hamming \
      -inputfile=$fwd \
      -inputfile=$rev \
      -resultfile=$fwd_kar \
      -resultfile=$rev_kar \
      -refgenomefile=$assembly \
      -alignfile=$aln \
      -evalfile=$eval 2> $log_eval
