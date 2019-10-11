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
data_dir='/storage/brno3-cerit/home/kika/pelomyxa/predicted_proteins_transdecoder/'

#copy files to zoli's folder
cp $data_dir'pelo.mit_predicted.fa' $diamond_dir

query='pelo.mit_predicted.fa'
db='nr2.dmnd'
out='pelo.mit_predicted.dmnd_bp.out'


#compute in zoli's folder
cd $diamond_dir
./diamond blastp -p $PBS_NUM_PPN -d $db -q $query -o $out -f 6 qseqid sseqid stitle evalue bitscore full_sseq --sensitive --max-target-seqs 1 --evalue 1e-5

#copy files back
cp $out $data_dir/.
