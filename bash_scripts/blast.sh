#!/bin/bash

cd '/Users/kika/ownCloud/membrane-trafficking/clathrin/fornicates_basks/9-BaSks_genomes/'

program=tblastn
task=tblastn
query='/Users/kika/ownCloud/membrane-trafficking/clathrin/fornicates_basks/fornicates_aCLC.fa'
db='/Users/kika/data/BaSk/blastdbs/Skoliomonas_sp_RCL.GCA_040285805.1_ASM4028580v1_genomic.fna'
out='SspRCL_forn.blast.tsv'
evalue=1e-05
outfmt=5
max_seqs=1
max_hsps=1
threads=6

$program -task $task \
	-query $query \
	-db $db \
	-out $out \
	-outfmt '6 qseqid qlen sseqid stitle slen length evalue pident bitscore mismatch gaps qstart qend sstart send' \
	-num_threads $threads \
	-evalue $evalue \
	-max_target_seqs $max_seqs \
	-max_hsps $max_hsps
