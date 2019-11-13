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
cp $data'37all_trimmed_1.fq.gz' $data'37all_trimmed_2.fq.gz' $SCRATCHDIR

assembly='Trinity_job_11485672.fasta'
fw='37all_trimmed_1.fq.gz'
rv='37all_trimmed_2.fq.gz'

sam=$out_dir'cther_37_bbmap_rna.sam'
rpkm=$out_dir'cther_37_bbmap.rpkm'
report=$out_dir'cther_37_bbmap.report'


#compute on scratch
cd $SCRATCHDIR
bbmap.sh in=$fw in2=$rv out=$sam ref=$assembly rpkm=$rpkm threads=$PBS_NUM_PPN 2> $report

#copy files back
rm $assembly $fw $rv
cp -r * $data
