#!/bin/sh

# raw_dir='/home/kika/'
# fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip -O $raw_dir SRR2048652

module add conda/modules
conda activate sra-tools-3.0.3

cd '/storage/brno3-cerit/home/kika/amoebophrya/'
wget https://sra-pub-run-odp.s3.amazonaws.com/sra/SRR1610334/SRR1610334
echo 'SRA SRR1610334 downloaded'
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip SRR1610334
echo 'SRA SRR1610334 split to pair-end files'
echo '-----------------------------'
echo

