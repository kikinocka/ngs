#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N diamond-bx
#PBS -l nodes=1:ppn=20
#PBS -l walltime=100:00:00

cd '/mnt/data/kika/blastocrithidia/possible_cont/'

db='/mnt/data/diamond_nr/prot.accession2taxid.FULL'
program=blastx
eval=1e-10
max_seqs=1
max_hsps=1

for query in *.fa; do
	echo $query
	out=${query%.fa}'.nr_'$eval'.diamond_'$program
	echo 'diamond $program \
		-q $query \
		-d $db \
		-o $out \
		--sensitive \
		-p 20 \
		-f "6 qseqid staxids bitscore std" \
		--evalue $eval \
		--max-target-seqs $max_seqs \
		--max_hsps $max_hsps"'
	# diamond $program \
	# 	-q $query \
	# 	-d $db \
	# 	-o $out \
	# 	--sensitive \
	# 	-p 20 \
	# 	-f "6 qseqid staxids bitscore std" \
	# 	--evalue $eval \
	# 	--max-target-seqs $max_seqs \
	# 	--max_hsps $max_hsps
	# echo ***Diamond done***
done
