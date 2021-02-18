#!/bin/bash

task=blastp
query='/mnt/mokosz/home/kika/mastigella_eilhardi_MAST/Mastigella_150316_prot.fas_50'
out='/mnt/mokosz/home/kika/mastigella_eilhardi_MAST/Mastigella_150316_prot.fas_50.dmnd.out'
db='/opt/databases/nr_auto/2021-02-15/diamond/nr.dmnd'
taxify='/mnt/mokosz/home/kika/rhizomastix_reassembly/taxify_DMND_nr_gz.py'
# outfmt=5
eval=1e-5
max_seqs=20
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
