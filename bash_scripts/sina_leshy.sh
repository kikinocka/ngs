#!/bin/bash

sina='/mnt/mokosz/home/kika/tools/sina-1.2.11/sina'

database='/mnt/mokosz/home/kika/silva_ssu_ref-nr90/SILVA_138.1_SSURef_NR99_12_06_20_opt.arb'
fasta='/mnt/mokosz/home/kika/workdir/metamonads_eukref_V9.fa'
fasta='/mnt/mokosz/home/kika/workdir/metamonads_eukref_V9.silva.aln'

$sina -i $fasta --intype fasta -o $aln --outtype fasta --ptdb $database
