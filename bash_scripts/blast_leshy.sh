#!/bin/bash

datadir='/mnt/mokosz/home/kika/pelomyxa_schiedti/peroxisomes/'
query=$datadir'pelomyxa_predicted_proteins.possibly_peroxisomal.fa'
out=$datadir'pelo.possibly_peroxisomal.nr.blast.xml'
db='/opt/databases/nr/nr'
program=blastp
task=blastp
outfmt=5
eval=1e-3
max_seqs=1
cpu=8

$program -task $task \
	-query $query \
	-db $db \
	-out $out \
	-outfmt $outfmt \
	-num_threads $cpu \
	-evalue $eval \
	-max_target_seqs $max_seqs \
