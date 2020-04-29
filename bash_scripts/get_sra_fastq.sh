#!/bin/sh

# raw_dir='/home/kika/'
# fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip -O $raw_dir SRR2048652

module add sratools-2.3.2

cd '/storage/brno3-cerit/home/kika/prototheca'
wget https://sra-downloadb.be-md.ncbi.nlm.nih.gov/sos/sra-pub-run-2/SRR8447028/SRR8447028.1
echo 'SRA SRR8447028.1 downloaded'
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip ./SRR8447028.1
echo 'SRA SRR8447028.1 split to pair-end files'
echo '-----------------------------'
echo

