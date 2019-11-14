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
cp $data'23all_1.fq.gz' $data'23all_2.fq.gz' $SCRATCHDIR

assembly='TriTrypDB-46_LseymouriATCC30220_AnnotatedCDSs.fasta'
fw='23all_1.fq.gz'
rv='23all_2.fq.gz'

sam=$out_dir'lsey_23_bbmap_rna.sam'
rpkm=$out_dir'lsey_23_bbmap.rpkm'
report=$out_dir'lsey_23_bbmap.report'


#compute on scratch
cd $SCRATCHDIR
bbmap.sh in=$fw in2=$rv out=$sam ref=$assembly rpkm=$rpkm threads=$PBS_NUM_PPN 2> $report

#copy files back
rm $assembly $fw $rv
cp -r * $data
