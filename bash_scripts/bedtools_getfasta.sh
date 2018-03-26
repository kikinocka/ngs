#!/bin/bash

genome='/media/4TB1/blastocrithidia/transcriptome_assembly/trinity_denovo/blobtools/lhes1/bexlh1_strict.fa'
gff='/media/4TB1/blastocrithidia/orthofinder/sg_ogs/alignments/jac_renamed/bexlh_only_ins_renamed.gff'
out='/media/4TB1/blastocrithidia/orthofinder/sg_ogs/alignments/jac_renamed/bexlh_ins_nt.txt'

bedtools getfasta -s -name -fi $genome -bed $gff -fo $out
