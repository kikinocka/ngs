#!/bin/bash

datadir='/mnt/mokosz/home/kika/workdir/'
query=$datadir'Ammonia.fa'
out=$datadir'Ammonia.eukprot.blast.xml'
db='/opt/databases/eukprot/current/blast/eukprot'
program=blastp
task=blastp
outfmt=5
eval=1e-02
max_seqs=20
max_hsps=1
cpu=8

$program -task $task \
	-query $query \
	-db $db \
	-out $out \
	-outfmt $outfmt \
	-num_threads $cpu \
	-evalue $eval \
	# -outfmt "6 qseqid staxids bitscore sseqid qcovs pident" \
	# -max_target_seqs $max_seqs \
	# -max_hsps $max_hsps \

