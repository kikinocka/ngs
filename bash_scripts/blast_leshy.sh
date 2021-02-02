#!/bin/bash

datadir='/mnt/mokosz/home/kika/rhizomastix_reassembly/'
query=$datadir'rhizomastix_reassembly.trinity.fa'
out=$datadir'rhizomastix_reassembly.nt.blast.out'
db='/opt/databases/nt_auto/current/blast'
program=blastn
task=blastn
# outfmt=5
outfmt=' "6 qseqid staxids bitscore sseqid qcovs pident" '
eval=1e-2
max_seqs=20
max_hsps=1
cpu=4

$program -task $task \
	-query $query \
	-db $db \
	-out $out \
	-outfmt $outfmt \
	-num_threads $cpu \
	-evalue $eval \
	-max_target_seqs $max_seqs \
	-max_hsps $max_hsps \

