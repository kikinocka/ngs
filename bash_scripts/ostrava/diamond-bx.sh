#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N diamond-bx
#PBS -l nodes=1:ppn=20
#PBS -l walltime=100:00:00

cd '/mnt/data/kika/blastocrithidia/possible_cont/'

db='/mnt/data/diamond_nr/nr.dmnd'
map='/mnt/data/diamond_nr/prot.accession2taxid.FULL'
program=blastx
eval=1e-10
max_seqs=1
max_hsps=1

for query in *.fa; do
	echo $query
	out=${query%.fa}'.nr_'$eval'.diamond_'$program
	diamond $program \
		-q $query \
		-d $db \
		-o $out \
		--taxonmap $map\
		--sensitive \
		-p 20 \
		-f "6 qseqid sseqid stitle sphylums staxids pident scovhsp qcovhsp length mismatch gapopen qstart qend sstart send evalue bitscore" \
		--evalue $eval \
		--max-target-seqs $max_seqs \
		--max-hsps $max_hsps
	echo ***Diamond done***
done
