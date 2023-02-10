#!/bin/bash

cmbuild='/Users/kika/miniconda3/pkgs/infernal-1.1.4-pl5321ha5712d3_1/bin/cmbuild'

cd '/Users/kika/programs/tRNAscan-SE_CM_alignments/isotype_specific/Eukaryota/'
aln='euk-Gln.sto'
cmfile='euk-Gln.CM.out'

$cmbuild $cmfile $aln
