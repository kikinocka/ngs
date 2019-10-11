#!/bin/sh
#PBS -N Diamond-bp
#PBS -l select=1:ncpus=10:mem=50gb:scratch_local=100gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add modules
module add diamond-0.8.29
module add python36-modules-gcc

diamond_dir='/storage/brno3-cerit/home/fussyz01/DMND/'
datadir='/storage/brno3-cerit/home/kika/diplonema/catalase/apx_tree/ver17/'

#copy files to scratch
cp $diamond_dir'diamond' $SCRATCHDIR || exit 1
cp $diamond_dir'refseq_excavata.dmnd' $SCRATCHDIR || exit 1
cp $datadir'1618.fa' $SCRATCHDIR || exit 1

db='refseq_excavata.dmnd'
query='1618.fa'
out='1618.dmnd_bp.out'

#compute on scratch
cd $SCRATCHDIR
./diamond blastp -p $PBS_NUM_PPN -d $db -q $query -o $out -f 6 qseqid sseqid stitle evalue bitscore full_sseq --sensitive --max-target-seqs 30 --evalue 1e-3

cp $out $diamond_dir
cd $diamond_dir
python diamondparse.py --pool True
