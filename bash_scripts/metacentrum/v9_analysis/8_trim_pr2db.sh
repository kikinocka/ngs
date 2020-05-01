#!/bin/bash
#PBS -N trim_pr2db
#PBS -l select=1:ncpus=15:mem=10gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add python36-modules-gcc

# # download the UTAX version and extract the V4 region
# VERSION="4.10.0"
# URL="https://github.com/vaulot/pr2_database/releases/download"
# SOURCE="pr2_version_${VERSION}_UTAX.fasta"
# wget "${URL}/${VERSION}/${SOURCE}.gz"
# gunzip -k ${SOURCE}.gz

# PRIMER_F="CCAGCASCYGCGGTAATTCC"
# PRIMER_R="TYRATCAAGAACGAAAGT"
# OUTPUT="${SOURCE/_UTAX*/}_${PRIMER_F}_${PRIMER_R}.fas"
# LOG="${OUTPUT/.fas/.log}"
# MIN_LENGTH=32
# MIN_F=$(( ${#PRIMER_F} * 2 / 3 ))
# MIN_R=$(( ${#PRIMER_R} * 2 / 3 ))
# CUTADAPT="$(which cutadapt) --discard-untrimmed --minimum-length ${MIN_LENGTH}"

# dos2unix < "${SOURCE}" | \
#     sed '/^>/ s/;tax=k:/ /
#          /^>/ s/,[dpcofgs]:/|/g
#          /^>/ ! s/U/T/g' | \
#     ${CUTADAPT} -g "${PRIMER_F}" -O "${MIN_F}" - 2> "${LOG}" | \
#     ${CUTADAPT} -a "${PRIMER_R}" -O "${MIN_R}" - 2>> "${LOG}" > "${OUTPUT}"