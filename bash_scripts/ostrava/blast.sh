#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N blast
#PBS -l nodes=1:ppn=10
#PBS -l walltime=900:00:00


cd '/mnt/data/kika/blastocrithidia/b_nonstop/'

query='bnonstop_predicted_proteins.fasta'
out='bnonstop_predicted_proteins.blast.tsv'
db='/mnt/data/kika/kineto_refs/blastDB/kinetoplastid_refs.TriTrypDB-61.fa'
program=blastp
task=blastp
eval=1e-20
max_seqs=1
max_hsps=1

$program -task $task \
	-query $query \
	-db $db \
	-out $out \
	-outfmt 6 \
	-num_threads 10 \
	-evalue $eval \
	-max_target_seqs $max_seqs \
	-max_hsps $max_hsps
	# -outfmt "6 qseqid staxids bitscore sseqid qcovs pident" \
	# -outfmt 5 \

python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: BLAST done
