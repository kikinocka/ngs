#!/bin/bash
#PBS -N filter_aln
#PBS -l select=1:ncpus=15:mem=25gb:scratch_local=50gb
#PBS -l walltime=02:00:00
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

datadir='/storage/brno3-cerit/home/kika/pelomyxa/mapping/tophat2/for_augustus2/'
cd $SCRATCHDIR

# #1) FILTER RAW ALIGNMENTS (~1.5h, 22 GB)
# cp $datadir'accepted_hits.bam' $SCRATCHDIR
# bam='accepted_hits.bam'
# sorted='accepted_hits.s.bam'
# filtered='accepted_hits.sf.bam'
# header='accepted_hits.header.txt'

# samtools sort -n $bam -@ PBS_NUM_PPN -o $sorted
# filterBam --uniq --paired --in $sorted --out $filtered
# # samtools view -H $filtered > $header
# cp $SCRATCHDIR/augustus_configs/extrinsic/extrinsic.M.RM.E.W.cfg $datadir/.

#2) CREATE INTRON HINTS (~5 min)
cp $datadir'accepted_hits.sf.bam' $SCRATCHDIR
cp $datadir'extrinsic.M.RM.E.W.cfg' $SCRATCHDIR/augustus_configs/extrinsic/.
bam='accepted_hits.sf.bam'
both='accepted_hits.both.ssf.bam'
hints='accepted_hits.introns.gff'

samtools sort $bam -@ PBS_NUM_PPN -o $both
bam2hints --intronsonly --minintronlen=30 --maxintronlen=2000 --in=$both --out=$hints
cp $SCRATCHDIR/augustus_configs/extrinsic/extrinsic.M.RM.E.W.cfg $datadir/extrinsic.cfg
cp -r $SCRATCHDIR/augustus_configs/* $augustus_configs/.

#copy files back
rm -r augustus_configs
rm $bam
cp -r * $datadir || export CLEAN_SCRATCH=false
