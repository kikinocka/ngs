#!/bin/bash

datadir='/mnt/mokosz/home/zoli/proj/Euglena_v2/'
program=tblastn
query=$datadir'plastid/plastid_stuff.fasta'
# outfmt=7
# word=3
files=$datadir'databases/*.fasta'

for db in $files; do
	echo $db
	out=${db%.*}'.tblastn.out'
	$program -query $query -db $db -out $out -outfmt "6 qseqid staxids bitscore sseqid qcovs pident" -num_threads 8 -max_target_seqs 1
	echo ***BLAST done***
done

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py BLAST EG done
