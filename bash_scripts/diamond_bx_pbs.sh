#!/bin/bash
#PBS -N diamond-bx
#PBS -l select=1:ncpus=10:mem=50gb:scratch_local=100gb
#PBS -l walltime=10:00:00
#PBS -m ae
#PBS -j oe

#RUN IN ZOLI'S FOLDER !!!

cat $PBS_NODEFILE

#add module
module add diamond-0.8.29

diamond_dir='/storage/brno3-cerit/home/fussyz01/DMND/'
data_dir='/storage/brno3-cerit/home/kika/pelomyxa/transcriptome_assembly/'

#copy files to zoli's folder
cp $data_dir'pelomyxa_transcriptome_clean.fa' $diamond_dir

query='pelomyxa_transcriptome_clean.fa'
db='refseq_ryby.dmnd'
out='pelo_clean_dmnd_bx.out'


#compute in zoli's folder
cd $diamond_dir
diamond blastx -q $query -d $db -o $out -p $PBS_NUM_PPN -f 6 --sensitive --max-target-seqs 1 --evalue 1e-5

#copy files back
cp $out $data_dir'blobtools/pelo_clean/.' || export CLEAN_SCRATCH=false
