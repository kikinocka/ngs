#!/bin/bash

task=blastp
query='/mnt/mokosz/home/kika/rhizomastix_reassembly/rhizomastix_reassembly.trinity.NTfilt.fasta.transdecoder_dir/longest_orfs.pep'
out='/mnt/mokosz/home/kika/rhizomastix_reassembly/rhizomastix_reassembly.trinity.NTfilt.fasta.transdecoder_dir/longest_orfs.nr.dmnd.out'
db='/opt/databases/nr_auto/2021-02-15/diamond/nr.dmnd'
# outfmt=5
eval=1e-5
max_seqs=20
cpu=10

diamond $task \
	-q $query \
	-d $db \
	-o $out \
	--outfmt "6 qseqid bitscore sseqid qcovhsp pident qlen length" \
	--threads $cpu \
	--evalue $eval \
	--max-target-seqs $max_seqs \
	--sensitive
