#!/bin/bash

cd '/Users/kika/ownCloud/SL_Euglenozoa/V9/above99_decontaminated/stramenopiles/'

fasta='STR_5480seqs_230711_core_blast_min700bp.No_Chimera.align_V5.lineage.fa'
clustered='STR_5480seqs_230711_core_blast_min700bp.No_Chimera.align_V5.lineage.clstr'
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
