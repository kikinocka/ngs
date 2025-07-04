#!/bin/bash

cd '/Users/kika/ownCloud/diplonema/TCA_cycle/IDH_tree/ver4/'

fasta='refs.fa'
clustered='refs_clstr_2'
seqid=0.99
coverage=0.5
mode=0

mmseqs easy-cluster $fasta $clustered tmp --min-seq-id $seqid -c $coverage --cov-mode $mode


# --min-seq-id
# List matches above this sequence identity (for clustering)

# -c
# List matches above this fraction of aligned (covered) residues

# --cov-mode
# (0) bidirectional
# (1) target coverage
# (2) query coverage
# (3) target-in-query length coverage
