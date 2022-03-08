#!/bin/bash

datadir='/Users/kika/ownCloud/diplonema/pyruvate_metabolism/PDH/E3/ver8-clustered/'
fasta=$datadir'E3.fa'
clustered=$datadir'E3_clstr60'
seqid=0.6
coverage=0.5
mode=0

mmseqs easy-cluster $fasta $clustered tmp --min-seq-id $seqid --cov-mode $mode


# --min-seq-id
# List matches above this sequence identity (for clustering)

# -c
# List matches above this fraction of aligned (covered) residues

# --cov-mode
# (0) bidirectional
# (1) target coverage
# (2) query coverage
# (3) target-in-query length coverage
