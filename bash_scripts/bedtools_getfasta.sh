#!/bin/bash

genome='/media/4TB1/blastocrithidia/genome_assembly/jaculum_scaffolds.fa'
gff='/media/4TB1/blastocrithidia/orthofinder/sg_ogs/alignments/jac_renamed/jac_only_ins_renamed.gff'
out='/media/4TB1/blastocrithidia/orthofinder/sg_ogs/alignments/jac_renamed/jac_ins_nt.txt'

bedtools getfasta -s -name -fi $genome -bed $gff -fo $out
