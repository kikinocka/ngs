#!/bin/bash

cd '/mnt/mokosz/home/kika/mastigamoeba_abducta_CHOM1/'

db='/opt/databases/nt_auto/current/blast/nt'
program=blastn
task=blastn
# outfmt=5
eval=1e-02
max_seqs=5
max_hsps=1
cpu=4

for query in trinity_a*; do
	$program -task blastn \
		-query $query \
		-db $db \
		-out ${query}.blast \
		-num_threads $cpu \
		-evalue $eval \
		-outfmt "6 qseqid staxids bitscore sseqid qcovs pident" \
		-max_target_seqs $max_seqs \
		-max_hsps $max_hsps &
done

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py BLAST done
