#!/bin/bash
#PBS -N diamond-bp
#PBS -l select=1:ncpus=10:mem=50gb:scratch_local=100gb
#PBS -l walltime=2:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add diamond-0.8.29

diamond_dir='/storage/brno3-cerit/home/kika/refseq/'
data_dir='/storage/brno3-cerit/home/kika/proteromonas/peroxisomal/'

#copy files to db's folder
cp $data_dir'possibly_peroxisomal.fa' $diamond_dir

query='possibly_peroxisomal.fa'
db='refseq.dmnd'
out='peroxisomal.dmnd_bp.out'


#compute in db's folder
cd $diamond_dir
diamond blastp -p $PBS_NUM_PPN -d $db -q $query -o $out -f 6 qseqid sseqid stitle evalue bitscore --sensitive --max-target-seqs 1 --evalue 1e-3

#copy files back
rm $query
mv $out $data_dir/.
