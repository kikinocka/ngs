#!/bin/bash

cmalign='/Users/kika/miniconda3/pkgs/infernal-1.1.4-pl5321ha5712d3_1/bin/cmalign'
cmfile='/Users/kika/programs/tRNAscan-SE_CM_alignments/isotype_specific/Eukaryota/euk-Gln.CM.out'
cmaln='/Users/kika/programs/tRNAscan-SE_CM_alignments/isotype_specific/Eukaryota/euk-Gln.sto'

cd '/Users/kika/ownCloud/Gln-tRNA/opisthokonts/hg38-tRNAs/'
sequences='opistho_Gln-tRNA.final.fa'
out='hg38_Gln-tRNA.final.infernal.aln'

#first make covariance model (CM) file by infernal_cmbuild.sh
$cmalign --outformat afa --cpu 6 --mapali $cmaln $cmfile $sequences > $out
