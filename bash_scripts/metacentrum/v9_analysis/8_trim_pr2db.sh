#!/bin/bash
#PBS -N trim_pr2db
#PBS -l select=1:ncpus=15:mem=10gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add python36-modules-gcc

DATADIR='/storage/brno3-cerit/home/kika/pr2db/'

#copy files to scratch
cp $DATADIR'pr2_version_4.12.0_18S_taxo_long.fasta' $SCRATCHDIR 


#run on scratch
cd $SCRATCHDIR

SOURCE='pr2_version_4.12.0_18S_taxo_long.fasta'
PRIMER_F='CCAGCASCYGCGGTAATTCC'
PRIMER_R='TYRATCAAGAACGAAAGT'
OUTPUT='pr2_version_4.12.0_18S_taxo_trimmed.fas'
LOG='pr2_version_4.12.0_18S_taxo_trimmed.log}'
MIN_LENGTH=32
MIN_F=$(( ${#PRIMER_F} * 2 / 3 ))
MIN_R=$(( ${#PRIMER_R} * 2 / 3 ))
CUTADAPT='$(which cutadapt) --discard-untrimmed --minimum-length ${MIN_LENGTH} -j $$PBS_NUM_PPN'

dos2unix < '${SOURCE}' | \
	sed '/^>/ s/;tax=k:/ /
		 /^>/ s/,[dpcofgs]:/|/g
		 /^>/ ! s/U/T/g' | \
	${CUTADAPT} -g '${PRIMER_F}' -O '${MIN_F}' - 2> '${LOG}' | \
	${CUTADAPT} -a '${PRIMER_R}' -O '${MIN_R}' - 2>> '${LOG}' > '${OUTPUT}'

#copy files back
# rm $SOURCE
cp -r * $DATADIR
