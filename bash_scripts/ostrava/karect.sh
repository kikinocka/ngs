#!/bin/bash
#PBS -N karect
#PBS -l nodes=1:ppn=10
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe


cd '/mnt/data/kika/blastocrithidia/b_frustrata/reads/'
fwd='4FEM_trimmed_75_1.fq'
rev='4FEM_trimmed_75_2.fq'
log='Bfr.karect_correct.txt'

karect -correct -threads=10 -matchtype=hamming -celltype=diploid -inputfile=$fwd -inputfile=$rev 2> $log

# karect -align -threads=10 -matchtype=hamming \
#       -inputfile=/mnt/data/bojana/Genomic/Obscuromonas_eliasi/Obscuromonas_eliasi_trimmed/trimmed75/PNG74_trimmed_75_1.fq \
#       -inputfile=/mnt/data/bojana/Genomic/Obscuromonas_eliasi/Obscuromonas_eliasi_trimmed/trimmed75/PNG74_trimmed_75_1.fq \
#       -refgenomefile=/mnt/data/bojana/Genomic/Obscuromonas_eliasi/Obscuromonas_eliasi_assembled/trimmed75/scaffolds.l500.fasta \
#       -alignfile=O_eliasi_align.txt &> log_karect_align_o_eliasi.txt

# karect -eval -threads=10 -matchtype=hamming \
#       -inputfile=/mnt/data/bojana/Genomic/Obscuromonas_eliasi/Obscuromonas_eliasi_trimmed/trimmed75/PNG74_trimmed_75_1.fq \
#       -inputfile=/mnt/data/bojana/Genomic/Obscuromonas_eliasi/Obscuromonas_eliasi_trimmed/trimmed75/PNG74_trimmed_75_2.fq \
#       -resultfile=/mnt/data/bojana/Genomic/Obscuromonas_eliasi/Obscuromonas_eliasi_trimmed/trimmed75/karrect/karect_PNG74_trimmed_75_1.fq \
#       -resultfile=/mnt/data/bojana/Genomic/Obscuromonas_eliasi/Obscuromonas_eliasi_trimmed/trimmed75/karrect/karect_PNG74_trimmed_75_2.fq \
#       -refgenomefile=/mnt/data/bojana/Genomic/Obscuromonas_eliasi/Obscuromonas_eliasi_assembled/trimmed75/scaffolds.l500.fasta \
#       -alignfile=/mnt/data/bojana/Genomic/Obscuromonas_eliasi/Obscuromonas_eliasi_trimmed/trimmed75/O_eliasi_align.txt \
#       -evalfile=O_eliasi_eval.txt
