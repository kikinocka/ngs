#!/bin/bash

genome='/media/4TB1/blastocrithidia/transcriptome_assembly/trinity_denovo/triat_trinity.fasta'
gff='/media/4TB1/blastocrithidia/orthofinder/sg_ogs/alignments/jac_renamed/triat_only_ins_renamed.gff'
out='/media/4TB1/blastocrithidia/orthofinder/sg_ogs/alignments/jac_renamed/triat_ins_nt.txt'

bedtools getfasta -s -name -fi $genome -bed $gff -fo $out
