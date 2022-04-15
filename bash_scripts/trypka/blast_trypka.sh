#!/bin/bash
cd '/media/4TB1/blastocrithidia/new_3-UTR/p57_trinity_all/blast_genome/e-05/'

query='/media/4TB1/blastocrithidia/new_3-UTR/p57_trinity_all/Trinity.fasta'
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
	-word_size $word_size
	# -max_target_seqs $max_seqs \
	# -max_hsps $max_hsps
	# -outfmt "6 qseqid staxids bitscore sseqid qcovs pident" \
