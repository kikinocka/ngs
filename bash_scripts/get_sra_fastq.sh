#!/bin/sh

# raw_dir='/home/kika/'
# fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip -O $raw_dir SRR2048652


wget https://sra-downloadb.be-md.ncbi.nlm.nih.gov/sos/sra-pub-run-2/SRR2048653/SRR2048653.1
echo 'SRA SRR2048653.1 downloaded'
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip ./SRR2048653.1
echo 'SRA SRR2048653.1 split to pair-end files'
echo '-----------------------------'
echo

wget https://sra-downloadb.be-md.ncbi.nlm.nih.gov/sos/sra-pub-run-2/SRR2048654/SRR2048654.1
echo 'SRA SRR2048654.1 downloaded'
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip ./SRR2048654.1
echo 'SRA SRR2048654.1 split to pair-end files'
echo '-----------------------------'
echo

wget https://sra-downloadb.be-md.ncbi.nlm.nih.gov/sos/sra-pub-run-2/SRR2048655/SRR2048655.1
echo 'SRA SRR2048655.1 downloaded'
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip ./SRR2048655.1
echo 'SRA SRR2048655.1 split to pair-end files'
echo '-----------------------------'
echo

wget https://sra-downloadb.be-md.ncbi.nlm.nih.gov/sos/sra-pub-run-2/SRR2048656/SRR2048656.1
echo 'SRA SRR2048656.1 downloaded'
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip ./SRR2048656.1
echo 'SRA SRR2048656.1 split to pair-end files'
echo '-----------------------------'
echo

wget https://sra-downloadb.be-md.ncbi.nlm.nih.gov/sos/sra-pub-run-2/SRR2048657/SRR2048657.1
echo 'SRA SRR2048657.1 downloaded'
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip ./SRR2048657.1
echo 'SRA SRR2048657.1 split to pair-end files'
echo '-----------------------------'
echo
