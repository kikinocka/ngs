#!/bin/bash

cd '/mnt/mokosz/home/kika/workdir/forn-bask/'

# db='Spironucleus_salmonicda.faa'
query='Tpc1.fa'
program=blastp
task=blastp
# outfmt=5
# eval=1e-05
max_seqs=1
max_hsps=1
cpu=8

# #one query, one database
# $program -task $task \
# 	-query $query \
# 	-db $db \
# 	-out fwd_hits.rev_blast.tsv \
# 	-num_threads $cpu \
# 	-outfmt '6 qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send' \
# 	-max_target_seqs $max_seqs \
# 	-max_hsps $max_hsps
# 	# -evalue $eval \


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
		-out ${db%.faa}.ssal_CLC.fwd_blast.tsv \
		-num_threads $cpu \
		-outfmt '6 qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send' 
done
#-evalue $eval \


python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py BLAST done
