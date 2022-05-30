#!/bin/bash

sina='/mnt/mokosz/home/kika/tools/sina-1.2.11/sina'

database='/mnt/mokosz/home/kika/silva_ssu_ref-nr90/SILVA_138.1_SSURef_NR99_12_06_20_opt.arb'
fasta='/mnt/mokosz/home/kika/workdir/cestodes.fa'
aln='/mnt/mokosz/home/kika/workdir/cestodes.silva.aln'

$sina -i $fasta --intype fasta -o $aln --outtype fasta --ptdb $database


python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py SINA done
