#!/bin/bash
#PBS -N diamond-bp
#PBS -l select=1:ncpus=20:mem=50gb:scratch_local=50gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add diamond-0.8.29

db_dir='/storage/brno3-cerit/home/fussyz01/DMND/'
data_dir='/storage/brno3-cerit/home/kika/euglenophytes/'

#copy files to scratch
cp $db_dir'nr2.dmnd' $SCRATCHDIR/nr.dmnd
cp $data_dir'rhab_check.fa' $SCRATCHDIR

query='rhab_check.fa'
db='nr.dmnd'
out='rhab_check_dmnd_bp.out'


#compute on scratch
cd $SCRATCHDIR

diamond blastp -q $query -d $db -o $out -p $PBS_NUM_PPN -f 6 qseqid sseqid stitle evalue bitscore full_sseq \
--sensitive --max-target-seqs 5 --evalue 1e-5

#copy files back
rm $query $db
cp -r * $data_dir || export CLEAN_SCRATCH=false
