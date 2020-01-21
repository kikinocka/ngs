#!/bin/sh
#PBS -N bbmap_rpkm
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add bbmap-36.92

data='/storage/brno3-cerit/home/kika/lsey/'

#copy files to scratch
cp $data'TriTrypDB-46_LseymouriATCC30220_AnnotatedCDSs.fasta' $SCRATCHDIR
cp $data'14all_trimmed_1.fq.gz' $SCRATCHDIR
cp $data'14all_trimmed_2.fq.gz' $SCRATCHDIR

assembly='Trinity_job_11485672.fasta'
fw='14all_trimmed_1.fq.gz'
rv='14all_trimmed_2.fq.gz'
# all='el_reads_new.fa'

sam='lsey_14_bbmap_rna.sam'
rpkm='lsey_14_bbmap.rpkm'
report='lsey_14_bbmap.report'


#compute on scratch
cd $SCRATCHDIR
#separate read files
bbmap.sh in=$fw in2=$rv out=$sam ref=$assembly rpkm=$rpkm threads=$PBS_NUM_PPN 2> $report

#one read file
# bbmap.sh in=$all out=$sam ref=$assembly rpkm=$rpkm threads=$PBS_NUM_PPN 2> $report


#copy files back
rm $assembly $fw $rv
# rm $assembly $all
cp -r * $data
