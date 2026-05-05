#!/bin/bash
#PBS -N TransDecoder_longORFs
#PBS -l select=1:ncpus=1:mem=2gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module load transdecoder

data_dir='/storage/brno12-cerit/home/kika/trimastix/Tmar50_trinity/'

#copy files to scratch
cp $data_dir'Tmar50_trinity.fasta' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

transcriptome='Tmar50_trinity.fasta'
basename=${transcriptome%.fasta}

TransDecoder.LongOrfs -t $transcriptome -O $basename
#--genetic_code Euplotid

#copy files back
rm $transcriptome
cp -r * $data_dir && clean_scratch
