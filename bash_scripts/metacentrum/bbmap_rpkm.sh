#!/bin/sh
#PBS -N bbmap_rpkm
#PBS -l select=1:ncpus=20:mem=100gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module load bbmap

datadir='/storage/brno12-cerit/home/kika/kinetoplastids/AOX/transcriptomics/tbruc/'

#copy files to scratch
cp $datadir'TriTrypDB-68_TbruceiTREU927_AnnotatedCDSs.fasta' $SCRATCHDIR
cp $datadir'cBF/'*_trimmed.fq.gz $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR
assembly='TriTrypDB-68_TbruceiTREU927_AnnotatedCDSs.fasta'
# fw='p57_trimmed_1.fq.gz'
# rv='p57_trimmed_2.fq.gz'
all='tbruc.fq.gz'

cat *.fq.gz > $all

base=tbcBF.
sam=$base'sam'
rpkm=$base'rpkm_bbmap.tsv'
report=$base'report_bbmap.txt'

# #separate read files
# bbmap.sh ref=$assembly in=$fw in2=$rv out=$sam rpkm=$rpkm threads=$PBS_NUM_PPN 2> $report

#one read file
bbmap.sh ref=$assembly in=$all out=$sam rpkm=$rpkm threads=$PBS_NUM_PPN 2> $report


#copy files back
# rm $assembly $fw $rv
rm $assembly *fq.gz
cp -r * $datadir && clean_scratch
