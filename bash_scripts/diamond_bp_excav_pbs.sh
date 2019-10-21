#!/bin/sh
#PBS -N Diamond-bp
#PBS -l select=1:ncpus=10:mem=50gb:scratch_local=100gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add modules
module add diamond-0.8.29

diamond_dir='/storage/brno3-cerit/home/kika/dmnd/'
datadir='/storage/brno3-cerit/home/kika/diplonema/catalase/apx_tree/ver17/'

#copy files to scratch
cp $diamond_dir'excavata.dmnd' $SCRATCHDIR
cp $datadir'1618.fa' $SCRATCHDIR

db='excavata.dmnd'
query='1618.fa'
out='1618.excavata.dmnd_bp.out'

#compute on scratch
cd $SCRATCHDIR
diamond blastp -p $PBS_NUM_PPN -d $db -q $query -o $out -f 6 qseqid sseqid stitle evalue bitscore full_sseq --sensitive --max-target-seqs 30 --evalue 1e-3

#copy files back
cp $out $diamond_dir
