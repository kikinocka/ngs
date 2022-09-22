#!/bin/bash
#PBS -N karect
#PBS -l nodes=1:ppn=10
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe


cd '/mnt/data/kika/blastocrithidia/b_triatomae/'
assembly='spades_all_careful/scaffolds.fasta'
fwd='reads/triat_trimmed_1.fq'
rev='reads/triat_trimmed_2.fq'
fwd_kar='karect_eval/triat_trimmed_1_karect.fq'
rev_kar='karect_eval/triat_trimmed_2_karect.fq'
aln='karect_eval/Btr_aln.txt'
eval='karect_eval/Btr_eval.txt'
log_aln='karect_eval/Btr.karect_aln.txt'
log_eval='karect_eval/Btr.karect_eval.txt'

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
