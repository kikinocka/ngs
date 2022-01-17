#!/bin/bash

datadir='/mnt/mokosz/home/kika/workdir/'
query=$datadir'pbei_aceE.fa'
out=$datadir'pbei_aceE.blast.out'
db='/opt/databases/eukprot/current/blast/eukprot'
program=blastp
task=blastp
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
	# -max_target_seqs $max_seqs \
	# -max_hsps $max_hsps
	# -outfmt "6 qseqid staxids bitscore sseqid qcovs pident" \

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py BLAST done
