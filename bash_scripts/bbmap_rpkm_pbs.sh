#!/bin/sh
#PBS -N bbmap_rpkm
#PBS -l select=1:ncpus=20:mem=10gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add bbmap-36.92

data='/storage/brno3-cerit/home/kika/cther/'

#copy files to scratch
cp $data'Trinity_job_11485672.fasta' $SCRATCHDIR
cp $data'23all_trimmed_1.fq.gz' $data'23all_trimmed_2.fq.gz' $SCRATCHDIR

assembly='Trinity_job_11485672.fasta'
fw='23all_trimmed_1.fq.gz'
rv='23all_trimmed_2.fq.gz'

sam=$out_dir'lsey_23_bbmap_rna.sam'
rpkm=$out_dir'lsey_23_bbmap.rpkm'
report=$out_dir'lsey_23_bbmap.report'


#compute on scratch
cd $SCRATCHDIR
bbmap.sh in=$fw in2=$rv out=$sam ref=$assembly rpkm=$rpkm threads=$PBS_NUM_PPN 2> $report

#copy files back
rm $assembly $fw $rv
cp -r * $data
