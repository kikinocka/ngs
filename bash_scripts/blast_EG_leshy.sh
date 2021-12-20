#!/bin/bash

datadir='/mnt/mokosz/home/zoli/proj/Euglena_v2/plastid/'
query=$datadir'plastid_stuff.fasta'
out=$datadir'plastid_stuff.tblast.out'
db='/mnt/mokosz/home/zoli/proj/Euglena_v2/databases/Trinity-GG-nt.fasta'
program=tblastn
task=tblastn
# outfmt=5
eval=1e-05
max_seqs=1
max_hsps=1
cpu=8

$program -task $task \
	-query $query \
	-db $db \
	-out $out \
	# -outfmt $outfmt \
	-outfmt "6 qseqid staxids bitscore sseqid qcovs pident" \
	-num_threads $cpu \
	-evalue $eval \
	-max_target_seqs $max_seqs \
	-max_hsps $max_hsps

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py BLAST EG done
