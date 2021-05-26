#!/bin/bash
#PBS -N trim_pr2db
#PBS -l select=1:ncpus=1:mem=5gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add python27-modules-gcc
# module add python36-modules-gcc

DATADIR='/storage/brno3-cerit/home/kika/pr2db/4.13.0/'

#copy files to scratch
cp $DATADIR'pr2_version_4.13.0_18S_UTAX.fasta' $SCRATCHDIR 


#run on scratch
cd $SCRATCHDIR

SOURCE='pr2_version_4.13.0_18S_UTAX.fasta'

# #V4 primers
# PRIMER_F="CCAGCASCYGCGGTAATTCC"
# PRIMER_R="TYRATCAAGAACGAAAGT"

# #V9 primers
PRIMER_F="TTGTACACACCGCCC"
PRIMER_R="GTAGGTGAACCTGCNGAAGG"

OUTPUT="${SOURCE/_long*/}_${PRIMER_F}_${PRIMER_R}.fas"
LOG="${OUTPUT/.fas/.log}"
MIN_LENGTH=32
MIN_F=$(( ${#PRIMER_F} * 2 / 3 ))
MIN_R=$(( ${#PRIMER_R} * 2 / 3 ))
CUTADAPT="$(which cutadapt) --discard-untrimmed --minimum-length ${MIN_LENGTH} -j $PBS_NUM_PPN"

dos2unix < "${SOURCE}" | \
	sed '/^>/ s/;tax=k:/ /
		 /^>/ s/,[dpcofgs]:/|/g
		 /^>/ ! s/U/T/g' | \
	${CUTADAPT} -g "${PRIMER_F}" -O "${MIN_F}" - 2> "${LOG}" | \
	${CUTADAPT} -a "${PRIMER_R}" -O "${MIN_R}" - 2>> "${LOG}" > "${OUTPUT}"

#copy files back
rm $SOURCE
cp -r * $DATADIR
