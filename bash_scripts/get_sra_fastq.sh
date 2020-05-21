#!/bin/sh

# raw_dir='/home/kika/'
# fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip -O $raw_dir SRR2048652

module add sratools-2.3.2

cd '/storage/brno3-cerit/home/kika/kinetoplastids/lguy_genome/reads'
wget https://sra-downloadb.be-md.ncbi.nlm.nih.gov/sos1/sra-pub-run-1/SRR8179913/SRR8179913.1
echo 'SRA SRR8179913 downloaded'
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip SRR8179913
echo 'SRA SRR8179913 split to pair-end files'
echo '-----------------------------'
echo

