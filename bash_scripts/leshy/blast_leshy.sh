#!/bin/bash

cd '/tmp/kika/'

query='v9.no_chimera.2-14.fa'
out='v9.no_chimera.2-14.blast.xml'
# db='/opt/databases/eukprot/current/blast/eukprot'
# db='/opt/databases/nr_auto/current/nr'
db='/opt/databases/nt_auto/current/blast/nt'
program=blastn
task=blastn
outfmt=5
eval=1e-05
max_seqs=1
max_hsps=1
cpu=8

$program -task $task \
	-query $query \
	-db $db \
	-out $out \
	-outfmt $outfmt \
	-num_threads $cpu \
	-evalue $eval \
	-max_target_seqs $max_seqs \
	-max_hsps $max_hsps
	# -outfmt "6 qseqid staxids bitscore sseqid qcovs pident" \

mv $out '/mnt/mokosz/home/kika/workdir/'

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py BLAST done
