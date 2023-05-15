#!/bin/sh

# raw_dir='/home/kika/'
# fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip -O $raw_dir SRR2048652

module add sratools-2.3.2

cd '/storage/brno3-cerit/home/kika/kinetoplastids/lguy_genome/reads'
wget ftp://ftp.sra.ebi.ac.uk/vol1/srr/SRR817/003/SRR8179913
echo 'SRA SRR8179913 downloaded'
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip SRR8179913
echo 'SRA SRR8179913 split to pair-end files'
echo '-----------------------------'
echo

