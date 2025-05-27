#!/bin/bash

cd '/mnt/mokosz/home/kika/metamonads/ancestral_OGs/final_trees/'

# db='/opt/databases/eukprot/current/blast/eukprot'
# db='/opt/databases/nr_auto/current/nr'
db='/mnt/mokosz/home/kika/allDB/all.faa'
program=blastp
task=blastp
outfmt=5
eval=1e-05
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
# 
# 

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py BLAST done
