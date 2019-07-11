#!/bin/bash
#PBS -N diamond-bp
#PBS -l select=1:ncpus=8:mem=50gb:scratch_local=100gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

#RUN IN ZOLI'S FOLDER !!!

cat $PBS_NODEFILE

#add module
module add diamond-0.8.29

diamond_dir='/storage/brno3-cerit/home/fussyz01/DMND/'
data_dir='/storage/brno3-cerit/home/kika/euglenophytes/'

#copy files to zoli's folder
cp $data_dir'rhab_check.fa' $diamond_dir

query='rhab_check.fa'
db='nr2.dmnd'
out='rhab_check_dmnd_bp.out'


#compute in zoli's folder
cd $diamond_dir
./diamond blastp -p $PBS_NUM_PPN -d $db -q $query -o $out -f 6 qseqid sseqid stitle evalue bitscore full_sseq --sensitive --max-target-seqs 5 --evalue 1e-5

#copy files back
cp $out $data_dir/.
