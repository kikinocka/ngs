#!/bin/bash

cd '/mnt/mokosz/home/kika/workdir/'

# db='/opt/databases/eukprot/current/blast/eukprot'
db='/mnt/mokosz/home/kika/nr_auto/2025-10-04/nr'
# db='/mnt/mokosz/home/kika/allDB/all.faa'
program=blastp
task=blastp
outfmt=5
eval=1e-10
max_seqs=1
max_hsps=1
cpu=8

for query in *.fa; do
	echo $query
	out=${query%.fa}'.fwd_blast.tsv'
	$program -task $task \
		-query $query \
		-db $db \
		-out $out \
		-outfmt '6 qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send' \
		-num_threads $cpu \
		-max_target_seqs $max_seqs \
		-max_hsps $max_hsps \
		-evalue $eval
	echo ***BLAST done***
done


python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py BLAST done
