#!/bin/sh

# raw_dir='/home/kika/'
# fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip -O $raw_dir SRR2048652


# wget https://sra-downloadb.be-md.ncbi.nlm.nih.gov/sos/sra-pub-run-2/SRR2048653/SRR2048653.1
# echo 'SRA SRR2048653.1 downloaded'
module add sratools-2.3.2
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip /storage/brno3-cerit/home/kika/lsey/SRR2048653.1
echo 'SRA SRR2048653.1 split to pair-end files'
# mv SRR2048653.1* /storage/brno3-cerit/home/kika/lsey/.
# echo 'SRA SRR2048653.1 moved'
echo '-----------------------------'
echo

# wget https://sra-downloadb.be-md.ncbi.nlm.nih.gov/sos/sra-pub-run-2/SRR2048654/SRR2048654.1
# echo 'SRA SRR2048654.1 downloaded'
module add sratools-2.3.2
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip /storage/brno3-cerit/home/kika/lsey/SRR2048654.1
echo 'SRA SRR2048654.1 split to pair-end files'
# mv SRR2048654.1* /storage/brno3-cerit/home/kika/lsey/.
# echo 'SRA SRR2048654.1 moved'
echo '-----------------------------'
echo

# wget https://sra-downloadb.be-md.ncbi.nlm.nih.gov/sos/sra-pub-run-2/SRR2048655/SRR2048655.1
# echo 'SRA SRR2048655.1 downloaded'
module add sratools-2.3.2
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip /storage/brno3-cerit/home/kika/lsey/SRR2048655.1
echo 'SRA SRR2048655.1 split to pair-end files'
# mv SRR2048655.1* /storage/brno3-cerit/home/kika/lsey/.
# echo 'SRA SRR2048655.1 moved'
echo '-----------------------------'
echo

# wget https://sra-downloadb.be-md.ncbi.nlm.nih.gov/sos/sra-pub-run-2/SRR2048656/SRR2048656.1
# echo 'SRA SRR2048656.1 downloaded'
module add sratools-2.3.2
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip /storage/brno3-cerit/home/kika/lsey/SRR2048656.1
echo 'SRA SRR2048656.1 split to pair-end files'
# mv SRR2048656.1* /storage/brno3-cerit/home/kika/lsey/.
# echo 'SRA SRR2048656.1 moved'
echo '-----------------------------'
echo

# wget https://sra-downloadb.be-md.ncbi.nlm.nih.gov/sos/sra-pub-run-2/SRR2048657/SRR2048657.1
# echo 'SRA SRR2048657.1 downloaded'
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip /storage/brno3-cerit/home/kika/lsey/SRR2048657.1
module add sratools-2.3.2
echo 'SRA SRR2048657.1 split to pair-end files'
# mv SRR2048657.1* /storage/brno3-cerit/home/kika/lsey/.
# echo 'SRA SRR2048657.1 moved'
echo '-----------------------------'
echo
