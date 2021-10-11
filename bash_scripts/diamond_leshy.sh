#!/bin/bash

cd '/mnt/mokosz/home/kika/beta-barrels/'

task=blastp
query='ena.beta-barrel.fa'
out='ena.beta-barrel.dmnd.out'
db='/opt/databases/nr_auto/2021-02-15/diamond/nr.dmnd'
taxify='/mnt/mokosz/home/kika/scripts/py_scripts/taxify_DMND_nr_gz.py'
# outfmt=5
eval=1e-3
max_seqs=1
cpu=10

diamond $task \
	-q $query \
	-d $db \
	-o $out \
	--outfmt 6 qseqid bitscore sseqid qcovhsp pident qlen length \
	--threads $cpu \
	--evalue $eval \
	--max-target-seqs $max_seqs \
	--sensitive

python2 $taxify -i $out 
