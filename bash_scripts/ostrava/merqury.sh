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
out='Bfru_scaff.kat.out'
base='Bfru_scaff.'


cd $work_dir'merqury/'
cp $fwd $rev .

# #get the right k size
# gsize=38237037
# $merqury'best_k.sh' $gsize

k=17.5764

#build meryl dbs
for each karect$i.fq ; do
    meryl k=$k count output karect$i.meryl karect$i.fq 2> $base'meryl.log'
done
