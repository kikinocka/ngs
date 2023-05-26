#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N blast
#PBS -l nodes=1:ppn=10
#PBS -l walltime=900:00:00

cd '/mnt/data/kika/blastocrithidia/genomes/final_assemblies/translated/'

query='/mnt/data/kika/references/kinetoplastids/for_annotator/reference.fa'
program=blastp
task=blastp
eval=1e-03
# max_seqs=1
# max_hsps=1

for db in *.fa; do
	echo $query
	# out=${query%.fa}'.nr_'$eval'.'$program
	out=${db%.fa}'.ref_'$eval'.tsv'
	$program -task $task \
		-query $query \
		-db $db \
		-out $out \
		-outfmt '6 qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send' \
		-num_threads 10 \
		-evalue $eval \
		#-max_target_seqs $max_seqs \
		#-max_hsps $max_hsps
	echo ***BLAST done***
done

python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: BLAST done
