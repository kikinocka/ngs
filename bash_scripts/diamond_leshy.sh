#!/usr/bin/env python3

task=blastp
query='/mnt/mokosz/home/kika/rhizomastix_reassembly/rhizomastix_reassembly.trinity.NTfilt.fasta.transdecoder_dir/longest_orfs.pep'
out='/mnt/mokosz/home/kika/rhizomastix_reassembly/rhizomastix_reassembly.trinity.NTfilt.fasta.transdecoder_dir/longest_orfs.nr.dmnd.out'
db='/opt/databases/nr_auto/2021-02-15/diamond/nr.dmnd'
# outfmt=5
eval=1e-2
max_seqs=20
max_hsps=1
cpu=4

diamond $task \
	-q $query \
	-d $db \
	-o $out \
	--outfmt "6 qseqid staxids bitscore sseqid qcovs pident" \
	--threads $cpu \
	--evalue $eval \
	--max-target-seqs $max_seqs \
	--max-hsps $max_hsps \
	--sensitive
