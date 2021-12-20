#!/bin/bash

datadir='/mnt/mokosz/home/kika/workdir/'
query=$datadir'v9.no_chimera.above99.fa'
out=$datadir'v9.no_chimera.above99.blast.xml'
db='/opt/databases/nt_auto/current/blast/nt'
program=blastn
task=blastn
outfmt=5
eval=1e-05
max_seqs=1
max_hsps=1
cpu=8

$program -task $task \
	-query $query \
	-db $db \
	-out $out \
	-outfmt $outfmt \
	-num_threads $cpu \
	-evalue $eval \
	-outfmt $outfmt \
	-max_target_seqs $max_seqs \
	-max_hsps $max_hsps
	# -outfmt "6 qseqid staxids bitscore sseqid qcovs pident" \

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py BLAST done
