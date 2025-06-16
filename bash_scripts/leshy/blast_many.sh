#!/bin/bash

cd '/mnt/mokosz/home/kika/allDB/renamed/'

# db='/mnt/mokosz/home/kika/allDB/all.faa'
query='/mnt/mokosz/home/kika/workdir/CAD2217633.fasta'
program=blastp
task=blastp
# outfmt=5
eval=1e-05
max_seqs=1000
max_hsps=1
cpu=8

# #one query, one database
# $program -task $task \
# 	-query $query \
# 	-db $db \
# 	-out all_EAP.fwd_blast.tsv \
# 	-num_threads $cpu \
# 	-evalue $eval \
# 	-outfmt '6 qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send' \
# 	-max_target_seqs $max_seqs \
# 	# -max_hsps $max_hsps


# #many queries, one database
# for query in *.fa ; do
# 	echo $query
# 	$program -task $task \
# 		-query $query \
# 		-db $db \
# 		-out ${query%.fa}.fwd_blast.tsv \
# 		-num_threads $cpu \
# 		-evalue $eval \
# 		-outfmt '6 qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send' \
# 		-max_target_seqs $max_seqs
# 		# -max_hsps $max_hsps
# done

#one query, many databases
for db in *faa ; do
	echo $db
	$program -task $task \
		-query $query \
		-db $db \
		-out ${db%.faa}.CAD2217633.fwd_blast.tsv \
		-num_threads $cpu \
		-evalue $eval \
		-outfmt '6 qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send' 
done


python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py BLAST done
