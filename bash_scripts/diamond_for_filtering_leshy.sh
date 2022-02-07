#!/bin/bash

cd '/mnt/mokosz/home/kika/mastigella_eilhardi_MAST/'

task=blastp
query='mei_trinity_NT/mei.trinity.NTfilt.fasta.transdecoder_dir/longest_orfs.pep'
out='mei.trinity.NTfilt.dmnd.out'
db='/opt/databases/nr_auto/2021-02-15/diamond/nr.dmnd'
taxify='/mnt/mokosz/home/kika/scripts/py_scripts/taxify_DMND_nr_gz.py'
eval=1e-5
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

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py DMND done
