#!/bin/bash

datadir='/mnt/mokosz/home/kika/rhizomastix_reassembly/rhizomastix_reassembly.trinity.NTfilt.fasta.transdecoder_dir/'
query=$datadir'longest_orfs.pep'
out=$datadir'longest_orfs.nr.blast.out'
db='/opt/databases/nr_auto/current/blast/nr'
program=blastp
task=blastp
# outfmt=5
outfmt='"6 qseqid staxids bitscore sseqid qcovs pident"'
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

