#!/bin/bash
#PBS -N create_honts
#PBS -l select=1:ncpus=25:mem=50gb:scratch_local=100gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add samtools-1.3.1
module add augustus-3.3.1

#setting augustus config file environment variable
augustus_configs='/storage/brno3-cerit/home/kika/augustus_configs/'
mkdir $SCRATCHDIR/augustus_configs/
cp -r $augustus_configs/* $SCRATCHDIR/augustus_configs/ || exit 1
export AUGUSTUS_CONFIG_PATH=$SCRATCHDIR/augustus_configs
export PATH=$PATH:/software/augustus/3.3.1/src/bin:/software/augustus/3.3.1/src/scripts

datadir='/storage/brno3-cerit/home/kika/pelomyxa/mapping/tophat2/for_augustus/'
cd $SCRATCHDIR

# #1) FILTER RAW ALIGNMENTS
# cp $datadir'accepted_hits.bam' $SCRATCHDIR
# bam='accepted_hits.bam'
# sorted='accepted_hits.s.bam'
# filtered='accepted_hits.sf.bam'
# header='accepted_hits.header.txt'

# samtools sort -n $bam -@ PBS_NUM_PPN -o $sorted
# filterBam --uniq --paired --in $sorted --out $filtered
# samtools view -H $filtered > $header

#2) CREATE INTRON HINTS
cp $datadir'accepted_hits.sf.bam' $SCRATCHDIR
bam='accepted_hits.sf.bam'
both='accepted_hits.both.ssf.bam'
hints='accepted_hits.hints.gff'

samtools sort $bam -@ PBS_NUM_PPN $both
bam2hints --intronsonly --in=$both --out=$hints

#copy files back
rm -r augustus_configs
rm $bam
cp -r * $datadir || export CLEAN_SCRATCH=false
