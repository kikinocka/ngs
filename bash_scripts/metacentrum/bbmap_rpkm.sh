#!/bin/sh
#PBS -N bbmap_rpkm
#PBS -l select=1:ncpus=20:mem=100gb:scratch_local=80gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module load bbmap

datadir='/storage/brno12-cerit/home/kika/kinetoplastids/AOX/transcriptomics/pfran/'

#copy files to scratch
cp $datadir'braker/braker.codingseq' $SCRATCHDIR
cp $datadir'reads/'*_trimmed*.fq.gz $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR
assembly='braker.codingseq'
fw='pfran_trimmed_1.fq.gz'
rv='pfran_trimmed_2.fq.gz'
# all='tbruc.fq.gz'

cat *_trimmed_1.fq.gz > $fw
cat *_trimmed_2.fq.gz > $rv
# cat *.fq.gz > $all

base=pfran.
sam=$base'sam'
rpkm=$base'rpkm_bbmap.tsv'
report=$base'report_bbmap.txt'

#paired-end read files
bbmap.sh ref=$assembly in=$fw in2=$rv out=$sam rpkm=$rpkm threads=$PBS_NUM_PPN 2> $report

# #one read file
# bbmap.sh ref=$assembly in=$all out=$sam rpkm=$rpkm threads=$PBS_NUM_PPN 2> $report


#copy files back
# rm $assembly $fw $rv
rm $assembly *fq.gz
cp -r * $datadir && clean_scratch
