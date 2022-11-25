#!/bin/bash

datadir='/mnt/mokosz/home/kika/mastigella_eilhardi_MAST/'
query=$datadir'Trinity_Mastigella_150316_renamed_nucl.fasta'
out=$datadir'filtration-NR_20220127/mei_trinity.blast'
db='/opt/databases/nt_auto/current/blast/nt'
program=blastn
task=blastn
# outfmt=5
eval=1e-02
max_seqs=5
max_hsps=1
cpu=8

$program -task $task \
	-query $query \
	-db $db \
	-out $out \
	-num_threads $cpu \
	-evalue $eval \
	-outfmt "6 qseqid staxids bitscore sseqid qcovs pident" \
	-max_target_seqs $max_seqs \
	-max_hsps $max_hsps \

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py BLAST done
