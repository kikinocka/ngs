#!/bin/bash
cd '/media/4TB1/blastocrithidia/new_3-UTR/20220523_trinity/blast_genome/'

query='/media/4TB1/blastocrithidia/new_3-UTR/20220523_trinity/Trinity.fasta'
out='p57_transcriptome-genome.blast.xml'
db='/media/4TB1/blastocrithidia/genome_assembly/blastdb/bnonstop_corrected_assembly.fasta'
program=blastn
task=blastn
outfmt=5
eval=1e-5
word_size=7
max_seqs=1
max_hsps=1
cpu=30

$program -task $task \
	-query $query \
	-db $db \
	-out $out \
	-outfmt $outfmt \
	-num_threads $cpu \
	-evalue $eval \
	-word_size $word_size \
	-max_target_seqs $max_seqs \
	-max_hsps $max_hsps
