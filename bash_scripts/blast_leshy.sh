#!/bin/bash

datadir='/mnt/mokosz/home/kika/prototheca/'
query=$datadir'pzop_hits.fa'
out=$datadir'pzop_hits.nr.blast.xml'
db='/opt/databases/nr/nr'
program=blastx
task=blastx
outfmt=5
eval=1e-3
max_seqs=3
cpu=20

#run in DB folder
# cd $db_dir
$program -task $task \
	-query $query \
	-db $db \
	-out $out \
	-outfmt $outfmt \
	-num_threads $cpu \
	-evalue $eval \
	-max_target_seqs $max_seqs \
