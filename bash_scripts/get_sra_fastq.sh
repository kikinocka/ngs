#!/bin/sh

# raw_dir='/home/kika/'
# fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip -O $raw_dir SRR2048652

module add sratools-2.3.2

cd '/storage/brno3-cerit/home/kika/prototheca'
wget https://sra-download.ncbi.nlm.nih.gov/traces/sra75/SRR/008249/SRR8447028
echo 'SRA SRR8447028 downloaded'
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip ./SRR8447028
echo 'SRA SRR8447028 split to pair-end files'
echo '-----------------------------'
echo

