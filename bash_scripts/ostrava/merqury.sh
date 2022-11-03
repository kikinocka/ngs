#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N merqury
#PBS -l nodes=1:ppn=80
#PBS -l walltime=20:00:00

merqury='/home/users/kika/miniconda3/share/merqury/'
work_dir='/mnt/data/kika/blastocrithidia/b_frustrata/'
read_dir='/mnt/data/kika/blastocrithidia/b_frustrata/reads/'
contigs=$work_dir'spades_75_karect/contigs.fasta'
fwd=$read_dir'karect_4FEM_trimmed_75_1.fq'
rev=$read_dir'karect_4FEM_trimmed_75_2.fq'
base='Bfru_scaff.'


cd $work_dir'merqury/'

#get the right kmer size
touch 'best_k.out'
gsize=38237037
$merqury'best_k.sh' $gsize > 'best_k.out'
#getting the kmer decimal number from output
kmer_tmp="tail -1 best_k.out"
#rounding the kmer number to integer
kmer="$($kmer_tmp | awk '{print int($1+0.5)}')" 

#build meryl dbs
meryl k=$kmer count output ${fwd%.fq}.meryl $fwd 2> $base.meryl_dbs.out
meryl k=$kmer count output ${rev%.fq}.meryl $rev 2>> $base.meryl_dbs.out


