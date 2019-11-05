#!/bin/bash
#PBS -N tblastn
#PBS -l select=1:ncpus=10:mem=50gb:scratch_local=50gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blast+-2.7.1

datadir='/auto/brno3-cerit/nfs4/home/kika/elonga_bct_genomes/'
program=tblastn
query=$datadir'query.fa'
outfmt=7
word=3
files=$datadir'*.fna'

for db in files; do
	echo $db
	out=${db%.*}'.tblastn.out'
	$program -query $query -db $db -out $out -outfmt $outfmt -word_size $word -num_threads $PBS_NUM_PPN
	echo ***BLAST done***
done
