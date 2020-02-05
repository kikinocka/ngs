#!/bin/bash
#PBS -N cutadapt
#PBS -l select=1:ncpus=10:mem=50gb:scratch_local=50gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add python36-modules-gcc

data='/storage/brno3-cerit/home/kika/sl_euglenozoa/'
out_dir=$data'trimmed_cutadapt/'

#copy files to scratch
cp $data'/merged_reads/1_CACTGT_merged.fq.gz' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR
gzip -d '1_CACTGT_merged.fq.gz'

PRIMER_F='TTGTACACACCGCCC'
PRIMER_R='GTAGGTGAACCTGCNGAAGG'
ANTI_PRIMER_F='GGGCGGTGTGTACAA'
ANTI_PRIMER_R='CCTTCNGCAGGTTCACCTAC'

INPUT='1_CACTGT_merged.fq'
LOG='1_CACTGT_merged.cutadapt_report.txt'
OUT_FW='1_CACTGT_FW'
OUT_RV='1_CACTGT_RV'
OUT_ANTI_FW='1_CACTGT_ANTI_FW'
OUT_ANTI_RV='1_CACTGT_ANTI_RV'
OUT_FASTA='1_CACTGT_cutadapt.fa'

# Get reads containing forward primer
cutadapt --discard-untrimmed --format=fastq -g ${PRIMER_F} -j $PBS_NUM_PPN -o ${OUT_FW} ${INPUT} > ${LOG}

# Get reads containing reverse primer
cutadapt --discard-untrimmed --format=fastq -a ${PRIMER_R} -j $PBS_NUM_PPN -o ${OUT_RV} ${OUT_FW} >> ${LOG}

# Get reads containing anti-reverse primer (in 5' position)
cutadapt --discard-untrimmed --format=fastq -g ${ANTI_PRIMER_R} -j $PBS_NUM_PPN -o ${OUT_ANTI_FW} ${INPUT} >> ${LOG}

# Get reads containing anti-forward primer (in 3' position)
cutadapt --discard-untrimmed --format=fastq -a ${ANTI_PRIMER_F} -j $PBS_NUM_PPN -o ${OUT_ANTI_RV} ${OUT_ANTI_FW} >> ${LOG}

# Convert fastq to fasta (reverse-complement the second file)
(awk '(NR - 2) % 4 == 0' ${OUT_RV}
 awk '(NR - 2) % 4 == 0' ${OUT_ANTI_RV} | \
     tr "acgturykmbdhvACGTURYKMBDHV" "tgcaayrmkvhdbTGCAAYRMKVHDB" | rev) | \
     grep -v [^ACGTacgt] | awk '{printf ">a%d\n%s\n", NR, $1}' > ${OUT_FASTA}

# rm -f ${OUT_FW} ${OUT_ANTI_FW} ${OUT_RV} ${OUT_ANTI_RV}

#copy files back
rm $INPUT
cp * $out_dir
