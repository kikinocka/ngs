#!/bin/bash

datadir='/mnt/mokosz/home/kika/prototheca/'
query=$datadir'pwic_hits.fa'
out=$datadir'pwic_hits.nr.blast.xml'
db='/opt/databases/nr/nr'
program=blastx
task=blastx
outfmt=5
eval=1e-3
max_seqs=5
cpu=4

$program -task $task \
	-query $query \
	-db $db \
	-out $out \
	-outfmt $outfmt \
	-num_threads $cpu \
	-evalue $eval \
	-max_target_seqs $max_seqs \
