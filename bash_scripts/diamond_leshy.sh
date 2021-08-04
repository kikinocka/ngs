#!/bin/bash

task=blastp
query='/mnt/mokosz/home/kika/endolimax_nana/filtration2/enan_trinity.NTfilt.fasta.transdecoder_dir/longest_orfs.pep'
out='/mnt/mokosz/home/kika/endolimax_nana/filtration2/enan.trinity.NTfilt.dmnd.out'
db='/opt/databases/nr_auto/2021-02-15/diamond/nr.dmnd'
taxify='/mnt/mokosz/home/kika/scripts/py_scripts/taxify_DMND_nr_gz.py'
# outfmt=5
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
