#!/bin/bash
#PBS -N diamond-bp
#PBS -l select=1:ncpus=10:mem=50gb:scratch_local=100gb
#PBS -l walltime=10:00:00
#PBS -m ae
#PBS -j oe

#RUN IN ZOLI'S FOLDER !!!

cat $PBS_NODEFILE

#add module
module add diamond-0.8.29

diamond_dir='/storage/brno3-cerit/home/fussyz01/DMND/'
data_dir='/storage/brno3-cerit/home/kika/diplonema/catalase/apx_tree/ver17/'

#copy files to zoli's folder
cp $data_dir'1618.fa' $diamond_dir

query='1618.fa'
db='nr2.dmnd'
out='1618.dmnd_bp.out'


#compute in zoli's folder
cd $diamond_dir
./diamond blastp -p $PBS_NUM_PPN -d $db -q $query -o $out -f 6 qseqid sseqid stitle evalue bitscore full_sseq --sensitive --max-target-seqs 30 --evalue 1e-3

#copy files back
rm $query
mv $out $data_dir/.
