#!/bin/bash

in1='/media/4TB1/blastocrithidia/mapping/p57_RNA_to_DNA/p57_bw2_sorted.bam'
in2='/media/4TB1/blastocrithidia/mapping/p57_polyA_RNA_to_DNA/p57_polyA_bw2_sorted.bam'
out='/media/4TB1/blastocrithidia/mapping/p57_both_RNA_to_DNA/p57_both_libraries.bam'

samtools merge $out $in1 $in2