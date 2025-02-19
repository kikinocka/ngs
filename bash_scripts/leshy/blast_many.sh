#!/bin/bash

cd '/mnt/mokosz/home/kika/allDB/renamed/'

# db='/opt/databases/nt_auto/current/blast/nt'
query='/mnt/mokosz/home/kika/workdir/Adea_EAP.fasta'
program=blastp
task=blastp
# outfmt=5
eval=1e-05
max_seqs=5
max_hsps=1
cpu=8

# #many queries, one databases
# for query in trinity_a*; do
# 	$program -task $task \
# 		-query $query \
# 		-db $db \
# 		-out ${query}.blast \
# 		-num_threads $cpu \
# 		-evalue $eval \
# 		-outfmt '6 qseqid staxids bitscore sseqid qcovs pident' \
# 		-max_target_seqs $max_seqs \
# 		-max_hsps $max_hsps &
# done


#one query, many databases
for db in *faa ; do
	echo $db
	$program -task $task \
		-query $query \
		-db $db \
		-out ${db%.faa}.EAP.fwd_blast.tsv \
		-num_threads $cpu \
		-evalue $eval \
		-outfmt '6 qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send' \
done


# python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py BLAST done
